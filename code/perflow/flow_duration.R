data_tcp = read.csv(file="../../data/perflow/flow_tcp.csv", header=TRUE, sep=",")
data_udp = read.csv(file="../../data/perflow/flow_udp.csv", header=TRUE, sep=",")
data_other= read.csv(file="../../data/perflow/flow_other.csv", header=TRUE, sep=",")

tcp_durs = data_tcp$Duration
udp_durs = data_udp$Duration
other_durs = data_other$Duration
all_durs = c(tcp_durs, udp_durs, other_durs)

all_cdf = ecdf(all_durs)
tcp_cdf = ecdf(tcp_durs)
udp_cdf = ecdf(udp_durs)

#plot(all_cdf, col="red", type="S", main="CDF of flow duration of ALL, TCP, UDP flows", xlab="duration (s)", ylab="probability")
plot(all_cdf, col="red", main="CDF of flow duration of ALL, TCP, UDP flows", xlab="duration (s)", ylab="probability")
lines(tcp_cdf, col="blue")
lines(udp_cdf, col="green")
legend(200,0.2, legend=c("All", "TCP", "UDP"), col=c("red", "blue", "green"), lty=1)
dev.print(png, '../../plots/perflow/flowdur_all.png', width=500)

quit()
