# NOTES:
# This file is exactly the same as original with 2 modifications as follows:

# 1. every time we know a packet belongs to a flow (new or old),
#       add it's FRAME NUMBER (given by Wireshark csv export) to the END [5]
#       of the arrays containing flow info - flowTCP, flowUDP
#       This way, we can know which packets (by id) belong to a flow
# 2. Once the arrays are built, we dump the binary as a pickle for
#       future use as these are constant.

# This file excludes any modification for numpy etc that were made later on.
# because it was not needed for our purposes for this file.

import pickle
import csv

with open('packetdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    flowsTCP = []
    flowsUDP = []
    for row in csv_reader:
        if row["Protocol"] == 'TCP':
            flowExists = False
            src = row["Source"]
            dest = row["Destination"]
            srcPort = row["Info"].split(' > ')[0].split(' ')[0]
            destPort = row["Info"].split(' > ')[1].split(' ')[1]
            startTime = float(row["Time"])
            for flow in flowsTCP:
                if src in flow and dest in flow and srcPort in flow and destPort in flow:
                    flowExists = True
                    flow[5].append(row["No."])
                    break
            if not flowExists:
                flowsTCP.append([src, dest, srcPort, destPort, startTime, [row["No."]] ])
        if row["Protocol"] == 'UDP':
            flowExists = False
            src = row["Source"]
            dest = row["Destination"]
            srcPort = row["Info"].split(' > ')[0].split(' ')[0]
            destPort = row["Info"].split(' > ')[1].split(' ')[1]
            for flow in flowsUDP:
                if src in flow and dest in flow and srcPort in flow and destPort in flow:
                    flowExists = True
                    break
            if not flowExists:
                flowsUDP.append([src, dest, srcPort, destPort, [row["No."]] ])
    print('TCP Length ' + str(len(flowsTCP)))
    print('UDP Length ' + str(len(flowsUDP)))

    with open('tcpout.pickle', 'wb') as fp1:
        pickle.dump(flowsTCP, fp1)

    with open('udpout.pickle', 'wb') as fp2:
        pickle.dump(flowsUDP, fp2)
