data = read.csv(file="../../data/rtt/numpak/r1est.csv", header=FALSE, sep=",")

frame_number = log(data$V1)
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="log_10 Frame numbers", ylab="time (s)", main="Num. Packets - Rank 1 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue")
legend(13,0.15, legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/numpak/r1.png', width=500)

