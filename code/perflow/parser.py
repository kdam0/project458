import csv

flowsAll = []

with open('tcpdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        flowsAll.append(float(row["Duration"]) / float(row["Packets"]))

with open('udpdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        flowsAll.append(float(row["Duration"]) / float(row["Packets"]))


with open('all_arrivel_time.csv', mode='w', newline='') as allArrival:
    fieldnames = ['time']
    writer = csv.DictWriter(allArrival, fieldnames=fieldnames)
    writer.writeheader()
    for flow in flowsAll:
        writer.writerow({'time': flow})

with open('packetdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    flowsTCP = []
    flowsUDP = []
    for row in csv_reader:
        if row["Protocol"] == 'TCP':
            tcpFlowExists = False
            src = row["Source"]
            dest = row["Destination"]
            timeElapsed = float(row["Time delta from previous captured frame"])
            srcPort = row["Info"].split(' > ')[0].split(' ')[0]
            destPort = row["Info"].split(' > ')[1].split(' ')[1]
            for flow in flowsTCP:
                if src in flow and dest in flow and srcPort in flow and destPort in flow:
                    tcpFlowExists = True
                    flow[4] += timeElapsed
                    flow[5] += 1
                    break
            if not tcpFlowExists:
                flowsTCP.append([src, dest, srcPort, destPort, timeElapsed, 1])
        if row["Protocol"] == 'UDP':
            udpFlowExists = False
            src = row["Source"]
            dest = row["Destination"]
            timeElapsed = float(row["Time delta from previous captured frame"])
            srcPort = row["Info"].split(' > ')[0].split(' ')[0]
            destPort = row["Info"].split(' > ')[1].split(' ')[1]
            for flow in flowsUDP:
                if src in flow and dest in flow and srcPort in flow and destPort in flow:
                    udpFlowExists = True
                    flow[4] += timeElapsed
                    flow[5] += 1
                    break
            if not udpFlowExists:
                flowsUDP.append([src, dest, srcPort, destPort, timeElapsed, 1])

    flowsTCPTimeAverages = []
    flowsUDPTimeAverages = []

    for flow in flowsTCP:
        flowsTCPTimeAverages.append(flow[4] / flow[5])
    for flow in flowsUDP:
        flowsUDPTimeAverages.append(flow[4] / flow[5])


    with open('tcp_arrivel_time.csv', mode='w', newline='') as tcpArrival:
        fieldnames = ['time']
        writer = csv.DictWriter(tcpArrival, fieldnames=fieldnames)
        writer.writeheader()
        for flow in flowsTCPTimeAverages:
            writer.writerow({'time': flow})

    with open('udp_arrivel_time.csv', mode='w', newline='') as udpArrival:
        fieldnames = ['time']
        writer = csv.DictWriter(udpArrival, fieldnames=fieldnames)
        writer.writeheader()
        for flow in flowsUDPTimeAverages:
            writer.writerow({'time': flow})

    print(len(flowsTCPTimeAverages))
    print(len(flowsUDPTimeAverages))
