options("scipen" = 10)
data = read.csv(file="../../data/rtt/numpak/r1est.csv", header=FALSE, sep=",")

frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Num. Packets - Rank 1 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/numpak/r1.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/numpak/r2est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Num. Packets - Rank 2 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/numpak/r2.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/numpak/r3est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Num. Packets - Rank 3 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/numpak/r3.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/bytes/r1est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Total Bytes - Rank 1 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/bytes/r1.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/bytes/r2est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Total Bytes - Rank 2 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/bytes/r2.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/bytes/r3est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Total Bytes - Rank 3 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/bytes/r3.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/dur/r1est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Duration - Rank 1 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/dur/r1.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/dur/r2est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Duration - Rank 2 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/dur/r2.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/dur/r3est.csv", header=FALSE, sep=",")
frame_number = data$V1
rtt_sample = data$V2
rtt_est = data$V3

plot(frame_number, rtt_sample, type="l", xlab="Frame numbers", ylab="time (s)", main="Duration - Rank 3 - RTT Sample and RTT Estimate")
lines(frame_number, rtt_est, col="blue", type="l")
legend('topright', legend=c("Sample", "Estimate"), col=c("black", "blue"), lty=1)

dev.print(png, '../../plots/rtt/dur/r3.png', width=500)
dev.off()
