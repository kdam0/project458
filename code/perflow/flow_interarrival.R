tcp_times = read.csv(file="../../data/perpacket/tcp_arrivel_time.csv", header=TRUE, sep=",")

tcp_times_cdf = ecdf(tcp_times$time)

plot(tcp_times_cdf, col="black", main="CDF of TCP inter-arrival time of TCP flows", xlab="time (s)", ylab="probability")
dev.print(png, '../../plots/perflow/interarrival.png', width=500)

#quit()
