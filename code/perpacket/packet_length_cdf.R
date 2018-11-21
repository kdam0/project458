data_all= read.csv(file="../../data/perpacket/packet_lengths_all.csv", header=TRUE, sep=",")
data_ip = read.csv(file="../../data/perpacket/packet_lengths_ip.csv", header=TRUE, sep=",")
data_tcp = read.csv(file="../../data/perpacket/packet_lengths_tcp.csv", header=TRUE, sep=",")
data_udp = read.csv(file="../../data/perpacket/packet_lengths_udp.csv", header=TRUE, sep=",")
data_nonip = read.csv(file="../../data/perpacket/packet_lengths_nonip.csv", header=TRUE, sep=",")

all_counts = data_all$Count[-1]
ip_counts = data_ip$Count[-1]
tcp_counts = data_tcp$Count[-1]
udp_counts = data_udp$Count[-1]
nonip_counts = data_nonip$Count[-1]

all_probs = cumsum(all_counts)/data_all$Count[1]
ip_probs = cumsum(ip_counts)/data_ip$Count[1]
tcp_probs = cumsum(tcp_counts)/data_tcp$Count[1]
udp_probs = cumsum(udp_counts)/data_udp$Count[1]
udp_probs = cumsum(udp_counts)/data_udp$Count[1]
nonip_probs = cumsum(nonip_counts)/data_nonip$Count[1]

lengths = c(0,20,40,80,160,320,640,1280,2560,5120)
log_lengths = log(lengths,2)

plot(log_lengths, all_probs, col="red", type="S", main="CDF of packet lengths of ALL, IP, TCP, UDP, and NON-IP packets", xlab="log_2 packet lengths", ylab="probability")
lines(log_lengths, ip_probs, col="blue", type="S")
lines(log_lengths, tcp_probs, col="green", type="S")
lines(log_lengths, udp_probs, col="cyan", type="S")
lines(log_lengths, nonip_probs, col="pink", type="S")
legend(10,0.2, legend=c("All","IP", "TCP", "UDP", "Non-IP"), col=c("red", "blue", "green", "cyan", "pink"), lty=1)
dev.print(png, '../../plots/perpacket/packetsize_all.png', width=500)

quit()
