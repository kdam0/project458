#!/bin/bash

ranks=(1 2 3)
# manually set these two lines
streams=(11 12 8)
outdir="rtt/dur/"

for i in "${ranks[@]}"
do
	echo "getting RTT samples rank ${i}..."
	tshark -Y "tcp.stream == ${streams[$((i-1))]}" -r univ1_pt13 -Tfields -e frame.number -e tcp.analysis.ack_rtt -E header=y -E separator=, > $outdir/r${i}.csv
	#echo ${ipsa[$((i-1))]}

done
echo "done"
