"""
Simple HTTP server for the review page.
Serves review.html and proxies image requests from local disk.

Usage: python server.py [--port 8899]
"""
import http.server
import urllib.parse
import mimetypes
import argparse
from pathlib import Path

RESULTS_DIR = Path(__file__).parent

class ReviewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        # Serve images from disk
        if parsed.path == "/image":
            params = urllib.parse.parse_qs(parsed.query)
            img_path = params.get("path", [None])[0]
            if img_path and Path(img_path).exists():
                mime = mimetypes.guess_type(img_path)[0] or "image/jpeg"
                data = Path(img_path).read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", mime)
                self.send_header("Content-Length", len(data))
                self.send_header("Cache-Control", "max-age=86400")
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, f"Image not found: {img_path}")
            return

        # Serve review.html as default
        if parsed.path in ("/", "/review.html", "/index.html"):
            html_path = RESULTS_DIR / "review.html"
            if html_path.exists():
                data = html_path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", len(data))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, "review.html not found - run review.py first")
            return

        self.send_error(404)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8899)
    args = p.parse_args()

    server = http.server.HTTPServer(("0.0.0.0", args.port), ReviewHandler)
    print(f"Review server running at http://0.0.0.0:{args.port}")
    print(f"Tunnel with: ssh -L {args.port}:localhost:{args.port} <this-host>")
    print("Ctrl+C to stop")
    server.serve_forever()
