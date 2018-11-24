options("scipen" = 10)

all_times = read.csv(file="../../data/perflow/all_arrivel_time.csv", header=TRUE, sep=",")
tcp_times = read.csv(file="../../data/perflow/tcp_arrivel_time.csv", header=TRUE, sep=",")
udp_times = read.csv(file="../../data/perflow/udp_arrivel_time.csv", header=TRUE, sep=",")

all_cdf = ecdf(all_times$time)
tcp_cdf = ecdf(tcp_times$time)
udp_cdf = ecdf(udp_times$time)

plot(all_cdf, col="red", main="CDF of inter-arrival times of ALL, TCP, and UDP flows", xlab="time (s)", ylab="probability", xlim=c(0,0.001), ylim=c(0,1))
lines(tcp_cdf, col="blue")
lines(udp_cdf, col="green")
legend('bottomright', legend=c("ALL", "TCP", "UDP"), col=c("red", "blue", "green"), lty=1)
dev.print(png, '../../plots/perflow/interarrival_all.png', width=500)

#quit()
