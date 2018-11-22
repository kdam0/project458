tcp_times = read.csv(file="../../data/perflow/tcp_arrivel_time.csv", header=TRUE, sep=",")

tcp_cdf = ecdf(tcp_times$time)

plot(tcp_cdf, col="blue", main="CDF of inter-arrival times of TCP flows", xlab="time (s)", ylab="probability", xlim=c(0,0.002), ylim=c(0,1))
dev.print(png, '../../plots/perflow/interarrival_tcp.png', width=500)

#quit()
