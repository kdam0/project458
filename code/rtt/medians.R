options("scipen" = 10)
data = read.csv(file="../../data/rtt/part2/r1_est_medians.csv", header=TRUE, sep=",")

plot(data$startTime, data$medianEstRtt, type="l", xlab="Start Time", ylab="Median Est. RTT (s)", main="Rank 1 - Median Est. RTT vs. Start Time")

dev.print(png, '../../plots/rtt/part2/r1.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/part2/r2_est_medians.csv", header=TRUE, sep=",")

plot(data$startTime, data$medianEstRtt, type="l", xlab="Start Time", ylab="Median Est. RTT (s)", main="Rank 2 - Median Est. RTT vs. Start Time")

dev.print(png, '../../plots/rtt/part2/r2.png', width=500)
dev.off()

data = read.csv(file="../../data/rtt/part2/r3_est_medians.csv", header=TRUE, sep=",")

plot(data$startTime, data$medianEstRtt, type="l", xlab="Start Time", ylab="Median Est. RTT (s)", main="Rank 3 - Median Est. RTT vs. Start Time")

dev.print(png, '../../plots/rtt/part2/r3.png', width=500)
dev.off()

