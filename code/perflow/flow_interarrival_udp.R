udp_times = read.csv(file="../../data/perflow/udp_arrivel_time.csv", header=TRUE, sep=",")

udp_cdf = ecdf(udp_times$time)

plot(udp_cdf, col="black", main="CDF of inter-arrival times of UDP flows", xlab="time (s)", ylab="probability", xlim=c(0,0.002), ylim=c(0,1))
dev.print(png, '../../plots/perflow/interarrival_udp.png', width=500)

#quit()
