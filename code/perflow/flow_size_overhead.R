data_tcp = read.csv(file="../../data/perflow/flow_tcp.csv", header=TRUE, sep=",")

tcp_bytes = data_tcp$Bytes
tcp_packets = data_tcp$Packets

# eth + ip + tcp headers per packet
overhead = sum(14,20,20)
tcp_overhead_perflow = tcp_packets * overhead

tcp_overhead_ratio = tcp_overhead_perflow / tcp_bytes

tcp_cdf = ecdf(tcp_overhead_ratio)

plot(tcp_cdf, col="black", main="CDF of TCP overhead ratio of TCP flows", xlab="overhead ratio", ylab="probability")
dev.print(png, '../../plots/perflow/flowsize_overhead.png', width=500)

#quit()
