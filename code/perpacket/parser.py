import csv
import numpy as np
import matplotlib.pyplot as plt

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
            timeElapsed = float(row["Time delta from previous captured frame"])
            for flow in flowsTCP:
                if src in flow and dest in flow and srcPort in flow and destPort in flow:
                    flowExists = True
                    flow[4] += timeElapsed
                    flow[5] += 1
                    break
            if not flowExists:
                flowsTCP.append([src, dest, srcPort, destPort, timeElapsed, 1])
        # if row["Protocol"] == 'UDP':
        #     flowExists = False
        #     src = row["Source"]
        #     dest = row["Destination"]
        #     srcPort = row["Info"].split(' > ')[0].split(' ')[0]
        #     destPort = row["Info"].split(' > ')[1].split(' ')[1]
        #     for flow in flowsUDP:
        #         if src in flow and dest in flow and srcPort in flow and destPort in flow:
        #             flowExists = True
        #             break
        #     if not flowExists:
        #         flowsUDP.append([src, dest, srcPort, destPort])
    flowsTCPTimeAverages  = []    
    for flow in flowsTCP:
        flowsTCPTimeAverages.append(flow[4] / flow[5])
    with open('tcp_arrivel_time.csv', mode='w', newline='') as tcpArrival:
        fieldnames = ['time']
        writer = csv.DictWriter(tcpArrival, fieldnames=fieldnames)
        writer.writeheader()
        for flow in flowsTCPTimeAverages:
            writer.writerow({'time': flow})
    # num_bins = 20
    # counts, bin_edges = np.histogram (flowsTCPTimeAverages, bins=num_bins, normed=True)
    # cdf = np.cumsum (counts)
    # plt.plot (bin_edges[1:], cdf/cdf[-1])
    # plt.show()
    # print(flowsTCPTimeAverages)
    # print('UDP Length ' + str(len(flowsUDP)))
