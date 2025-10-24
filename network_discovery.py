import scapy.all as scapy
import argparse
import threading
import time

def scan_network(ip_range, timeout=2):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.sr(arp_request_broadcast, timeout=timeout, verbose=False)[0]

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for sent, received in answered_list:
        print(received.psrc + " "*18 + received.hwsrc)

def scan_network_threaded(ip_range, num_threads=4, timeout=2):
    threads = []
    ip_range_list = [ip_range[i:i+256] for i in range(0, 256*num_threads, 256)]
    for ip_subrange in ip_range_list:
        thread = threading.Thread(target=scan_network, args=(ip_subrange, timeout))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Discovery Tool")
    parser.add_argument("ip_range", help="IP range to scan (e.g., 192.168.1.0/24)")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads to use for scanning")
    parser.add_argument("--timeout", type=int, default=2, help="Timeout for ARP requests in seconds")
    args = parser.parse_args()

    scan_network_threaded(args.ip_range, args.threads, args.timeout)