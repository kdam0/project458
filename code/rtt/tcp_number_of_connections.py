import csv

flowsTCP = []
with open('packetdata.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["Protocol"] == 'TCP':
            tcpFlowExists = False
            src = row["Source"]
            dest = row["Destination"]
            for flow in flowsTCP:
                if src in flow and dest in flow:
                    tcpFlowExists = True
                    if row["Stream index"] not in flow[2]:
                        flow[2].append(row["Stream index"])
                    break
            if not tcpFlowExists:
                flowsTCP.append([src, dest, [row["Stream index"]]])

csv_file.close()

flowsTCPOut = []

for row in flowsTCP:
    flowsTCPOut.append([row[0], row[1], len(row[2])])

with open('tcp_number_of_connections.csv', mode='w', newline='') as tcpConnections:
    fieldnames = ['src', 'dest', 'connectionCount']
    writer = csv.DictWriter(tcpConnections, fieldnames=fieldnames)
    writer.writeheader()
    for flow in flowsTCPOut:
        writer.writerow({'src': flow[0], 'dest': flow[1], 'connectionCount': flow[2]})

tcpConnections.close()
