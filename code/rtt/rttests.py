import sys
import csv
import numpy

datapath = '../../data/rtt/'
subdirs = ['numpak/', 'bytes/', 'dur/']
filenames = ['r1', 'r2', 'r3']

# returns ['numpak r1-3, bytesr1-3, durr1-3'] of length 9
def readAllSamples():
    allSamples = []
    for sub in subdirs:
        for fname in filenames:
            fullpath = datapath + sub + fname + ".csv"
            sample = readsamepleRTTs(fullpath)
            allSamples.append(sample)
    return allSamples

def writeAllEstimates(allSamples, allEsts):
    counter = 0
    for sub in subdirs:
        for fname in filenames:
            fullpath = datapath + sub + fname + "est.csv"
            writeestRTTs(fullpath, allSamples[counter], allEsts[counter])
            counter += 1

def readsamepleRTTs(datapath):
    sampleRTT = []
    with open(datapath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # apply a sane filter
            if (row['tcp.analysis.ack_rtt'] != ""):
                sampleRTT.append( (int(row['frame.number']), float(row['tcp.analysis.ack_rtt'])) )
    csv_file.close()
    return sampleRTT

def writeestRTTs(datapath, samples, estimates):
    with open(datapath, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for i, sample in enumerate(samples):
            csv_writer.writerow([ sample[0], sample[1], estimates[i] ])
    csv_file.close()
    return 0

def calcEST(samples):
    ests = []
    K = 4
    G = 0.001 # =100 msec
    alpha = 1/8.0
    beta = 1/4.0

    # (2.1) of rtc6298
    RTO = 1.0
    counter = 1
    for sample in samples:
        R = sample[1]
        # (2.2) of rtc6298
        if counter == 1:
            SRTT = R
            RTTVAR = R / 2.0
        # (2.3) of rtc6298
        else:
            RTTVAR = (1.0 - beta) * RTTVAR + beta * abs(SRTT - R)
            SRTT = (1.0 - alpha) * SRTT + alpha * R

        RTO = SRTT + max(G, K * RTTVAR)
        # (2.4) of rtc6298
        RTO = max(1.0, RTO)
        ests.append(SRTT)
        counter += 1
    return ests

# returns ests in order = ['numpak r1-3, bytesr1-3, durr1-3'] of length 9
def calcAllEst(allSamples):
    allEsts = []
    for sample in allSamples:
        est = calcEST(sample)
        allEsts.append(est)
    return allEsts

all_samples = readAllSamples()
all_ests = calcAllEst(all_samples)
writeAllEstimates(all_samples, all_ests)

print("done")
