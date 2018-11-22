import pickle
import datetime
import sys
import dpkt

tcp_dump_filename   = 'tcpout.pickle'
pkts_dump_filename = 'pkts2.pickle'
pkts = []
flowsTCP = []

def create_pcap_to_pickle_dump():
    global pkts
    print("Reading pccp file ...")
    f = open("univ1_pt13", 'rb')
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        # we will store the frame, along with timestamp
        # as a tuple
        pkts.append((ts, eth))

    print("number of frames", len(pkts))
    print("Writing to pcap to pickle ...")
    with open('pkts2.pickle', 'wb') as fp3:
        pickle.dump(pkts, fp3)
    f.close()
    fp3.close()

def read_dump(filename):
    print("Reading pickle file " + filename + " ...")
    with open(filename, 'rb') as fp:
        py_arr = pickle.load(fp)
    fp.close()
    return py_arr

# will get a list of the starting frame for each flow
def get_flow_start_frame_nums():
    start_frame_nums = []
    for flow in flowsTCP:
        start_frame = flow[5][0]
        start_frame_nums.append(int(start_frame))
    return start_frame_nums

# will get a list of the ending frame for each flow
def get_flow_end_frame_nums():
    end_frame_nums = []
    for flow in flowsTCP:
        num_packs_in_flow = len(flow[5])
        end_frame = flow[5][num_packs_in_flow-1]
        end_frame_nums.append(int(end_frame))
    return end_frame_nums

# only used for detecting FINS
def get_last_two_end_frames():
    end_frame_nums = []
    for flow in flowsTCP:
        num_packs_in_flow = len(flow[5])
        if num_packs_in_flow > 1:
            end_frame = flow[5][num_packs_in_flow-1]
            sec_last_end_fram = flow[5][num_packs_in_flow-2]
            end_frame_nums.append((int(sec_last_end_fram), int(end_frame)))
    return end_frame_nums

# returns a count for 1 packet flows that end with syn only
def count_syns_only():
    count = 0
    for start_frame, end_frame in zip(start_frame_nums,end_frame_nums):
        if start_frame == end_frame:
            # only 1 packet in this flow, get the packet
            ts, eth_frame = pkts[end_frame]
            if hasattr(eth_frame, 'data'):
                ip = eth_frame.data
                if hasattr(ip, 'data'):
                    tcp = ip.data
                    if hasattr(tcp, 'flags'):
                        # check syn and ack for this packet
                        syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN ) != 0
                        ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK ) != 0
                        if syn_flag == 1 and ack_flag == 0:
                            count += 1
    return count

# returns a count of flows that ended with reset
def count_resets():
    count = 0
    for end_frame in end_frame_nums:
        ts, eth_frame = pkts[end_frame]
        if hasattr(eth_frame, 'data'):
            ip = eth_frame.data
            if hasattr(ip, 'data'):
                tcp = ip.data
                if hasattr(tcp, 'flags'):
                    # check reset flag for this packet
                    rst_flag = ( tcp.flags & dpkt.tcp.TH_RST ) != 0
                    if rst_flag == 1:
                        count += 1
    return count

# returns a count of flows that ended with Fin properly
def count_fins():
    count = 0
    for sec_last_frame, last_frame in two_end_frame_nums:
        ts_sl, eth_frame_sl = pkts[sec_last_frame]
        ts_ll, eth_frame_ll = pkts[last_frame]
        if hasattr(eth_frame_sl, 'data') and hasattr(eth_frame_ll, 'data'):
            ip_sl = eth_frame_sl.data
            ip_ll = eth_frame_ll.data
            if hasattr(ip_sl, 'data') and hasattr(ip_ll, 'data'):
                tcp_sl = ip_sl.data
                tcp_ll = ip_ll.data
                if hasattr(tcp_sl, 'flags') and hasattr(tcp_ll, 'flags'):
                    # check if fin and ack were sent by second last
                    # check if last acked it
                    fin_flag = ( tcp_sl.flags & dpkt.tcp.TH_FIN ) != 0
                    ack_flag = ( tcp_sl.flags & dpkt.tcp.TH_ACK ) != 0
                    ack_flag_ll = ( tcp_ll.flags & dpkt.tcp.TH_ACK ) != 0
                    if fin_flag == 1 and ack_flag == 1 and ack_flag_ll == 1:
                        count += 1
    return count

# returns a count of flows that have last packet within 5 mins of pcap start
def count_ongoing():
    count = 0
    first_frame_time = get_frame_timestamp(0)
    for end_frame in end_frame_nums:
        end_frame_time = get_frame_timestamp(end_frame)
        delta_s = (end_frame_time - first_frame_time).total_seconds()
        # check if within 5 mins
        if delta_s <= (5 * 60): count += 1
    return count

# returns a count of flows that have last packet before 5 mins of pcap start
# and some more checks for failure
def count_failed():
    count = 0
    first_frame_time = get_frame_timestamp(0)
    for end_frame in end_frame_nums:
        end_frame_time = get_frame_timestamp(end_frame)
        delta_s = (end_frame_time - first_frame_time).total_seconds()
        # check if beyond 5 mins
        if delta_s > (5 * 60):
            # check for some flags
            ts, eth_frame = pkts[end_frame]
            if hasattr(eth_frame, 'data'):
                ip = eth_frame.data
                if hasattr(ip, 'data'):
                    tcp = ip.data
                    if hasattr(tcp, 'flags'):
                        # check reset, and fin flag for this packet
                        rst_flag = ( tcp.flags & dpkt.tcp.TH_RST ) != 0
                        fin_flag = ( tcp.flags & dpkt.tcp.TH_FIN ) != 0
                        if rst_flag == 0 or fin_flag == 0:
                            count += 1

    return count

# returns a python datetime obj for a frame's timestamp
def get_frame_timestamp(frame_number):
    ts, eth = pkts[frame_number]
    time = datetime.datetime.utcfromtimestamp(ts)
    return time

# From dpkt docs...
# Source: http://www.commercialventvac.com/dpkt.html
# Author: Jeff Silverman, jeffsilverm at gmail dot com
# This function is not used anywhere, but some of the
#   lines are.
def decode_tcp_flags(tcp):
    fin_flag = ( tcp.flags & dpkt.tcp.TH_FIN ) != 0
    syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN ) != 0
    rst_flag = ( tcp.flags & dpkt.tcp.TH_RST ) != 0
    psh_flag = ( tcp.flags & dpkt.tcp.TH_PUSH) != 0
    ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK ) != 0
    urg_flag = ( tcp.flags & dpkt.tcp.TH_URG ) != 0
    ece_flag = ( tcp.flags & dpkt.tcp.TH_ECE ) != 0
    cwr_flag = ( tcp.flags & dpkt.tcp.TH_CWR ) != 0
    pass


# If first time running then run next line
# otherwise leave commented out:
# create_pcap_to_pickle_dump()

flowsTCP = read_dump(tcp_dump_filename);
pkts     = read_dump(pkts_dump_filename);

start_frame_nums   = get_flow_start_frame_nums()
end_frame_nums     = get_flow_end_frame_nums()
two_end_frame_nums = get_last_two_end_frames()

print("SYN count",     count_syns_only())
print("RESET count",   count_resets())
print("FIN count",     count_fins())
print("ONGOING count", count_ongoing())
print("FAILED count",  count_failed())
print("done")
