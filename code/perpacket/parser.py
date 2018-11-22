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
                    break
            if not flowExists:
                flowsTCP.append([src, dest, srcPort, destPort, startTime, startTime])
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
                flowsUDP.append([src, dest, srcPort, destPort])
    print('TCP Length ' + str(len(flowsTCP)))
    print('UDP Length ' + str(len(flowsUDP)))
