import csv
import os

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

def getEstMedians(indices):
    out = []
    indexCount = 1
    for streamIndex in indices:
        if indexCount > 400:
            break
        os.system("tshark  -Y \"tcp.stream == " + str(streamIndex) + "\" -T fields -e tcp.analysis.ack_rtt -e frame -E separator=, -E header=y -r univ1_pt13 > temp.csv")
        sampleRTT = []
        with open('temp.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # apply a sane filter
                if (row['tcp.analysis.ack_rtt'] != ""):
                    sampleRTT.append( (int(row['frame'].split(' ')[1][:-1]), float(row['tcp.analysis.ack_rtt'])) )
        csv_file.close()

        ests = calcEST(sampleRTT)
        ests.sort()
        length = len(ests)
        if (length % 2 == 0):
            median = (ests[(length)//2] + ests[(length)//2-1]) / 2
        else:
            median = ests[(length-1)//2]
        out.append([indexCount, median])
        print(indexCount)
        indexCount += 1
        os.remove('temp.csv')
    return out

def getStartTimes(indices, file):
    out = []
    indexCount = 1
    for streamIndex in indices:
        if indexCount > 400:
            break
        startTime = 10000000
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if int(row["Stream index"]) == streamIndex:
                    startTime = min(float(row["Time"]), startTime)
            out.append([indexCount, startTime])
        csv_file.close()
        indexCount += 1
    return out

# get start time values for each host pair

r1Indices = []
with open('r1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if int(row["Stream index"]) not in r1Indices:
            r1Indices.append(int(row["Stream index"]))
csv_file.close()
r1Indices.sort()

r1StartTimes = getStartTimes(r1Indices, 'r1.csv')
with open('r1_start_times.csv', mode='w', newline='') as r1_start_times_file:
    fieldnames = ['indexCount', 'startTime']
    writer = csv.DictWriter(r1_start_times_file, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r1StartTimes:
        writer.writerow({'indexCount': flow[0], 'startTime': flow[1]})
r1_start_times_file.close()

r2Indices = []
with open('r2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if int(row["Stream index"]) not in r2Indices:
            r2Indices.append(int(row["Stream index"]))
csv_file.close()
r2Indices.sort()

r2StartTimes = getStartTimes(r2Indices, 'r2.csv')
with open('r2_start_times.csv', mode='w', newline='') as r2_start_times_file:
    fieldnames = ['indexCount', 'startTime']
    writer = csv.DictWriter(r2_start_times_file, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r2StartTimes:
        writer.writerow({'indexCount': flow[0], 'startTime': flow[1]})
r1_start_times_file.close()

r3Indices = []
with open('r3.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if int(row["Stream index"]) not in r3Indices:
            r3Indices.append(int(row["Stream index"]))
csv_file.close()
r3Indices.sort()

r3StartTimes = getStartTimes(r3Indices, 'r3.csv')
with open('r3_start_times.csv', mode='w', newline='') as r3_start_times_file:
    fieldnames = ['indexCount', 'startTime']
    writer = csv.DictWriter(r3_start_times_file, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r3StartTimes:
        writer.writerow({'indexCount': flow[0], 'startTime': flow[1]})
r1_start_times_file.close()

# get median values for each host pair

r1EstMedians = getEstMedians(r1Indices)
r2EstMedians = getEstMedians(r2Indices)
r3EstMedians = getEstMedians(r3Indices)

with open('r1_est_medians.csv', mode='w', newline='') as estMedians:
    fieldnames = ['sequenceNumber', 'medianEstRtt']
    writer = csv.DictWriter(estMedians, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r1EstMedians:
        writer.writerow({'sequenceNumber': flow[0], 'medianEstRtt': flow[1]})
estMedians.close()

with open('r2_est_medians.csv', mode='w', newline='') as estMedians:
    fieldnames = ['sequenceNumber', 'medianEstRtt']
    writer = csv.DictWriter(estMedians, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r2EstMedians:
        writer.writerow({'sequenceNumber': flow[0], 'medianEstRtt': flow[1]})
estMedians.close()

with open('r3_est_medians.csv', mode='w', newline='') as estMedians:
    fieldnames = ['sequenceNumber', 'medianEstRtt']
    writer = csv.DictWriter(estMedians, fieldnames=fieldnames)
    writer.writeheader()
    for flow in r3EstMedians:
        writer.writerow({'sequenceNumber': flow[0], 'medianEstRtt': flow[1]})
estMedians.close()
