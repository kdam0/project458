data_tcp = read.csv(file="../../data/perflow/flow_tcp.csv", header=TRUE, sep=",")
data_udp = read.csv(file="../../data/perflow/flow_udp.csv", header=TRUE, sep=",")
data_other= read.csv(file="../../data/perflow/flow_other.csv", header=TRUE, sep=",")

tcp_bytes = data_tcp$Bytes
udp_bytes = data_udp$Bytes
other_bytes = data_other$Bytes
all_bytes = c(tcp_counts, udp_counts, other_counts)

all_cdf = ecdf(log(all_counts))
tcp_cdf = ecdf(log(tcp_counts))
udp_cdf = ecdf(log(udp_counts))

#plot(all_cdf, col="red", type="S", main="CDF of flow duration of ALL, TCP, UDP flows", xlab="duration (s)", ylab="probability")
plot(all_cdf, col="red", main="CDF of byte counts of ALL, TCP, UDP flows", xlab="log byte counts", ylab="probability")
lines(tcp_cdf, col="blue")
lines(udp_cdf, col="green")
legend(8,0.2, legend=c("All", "TCP", "UDP"), col=c("red", "blue", "green"), lty=1)
dev.print(png, '../../plots/perflow/flowsize_all_bytes.png', width=500)

#quit()
