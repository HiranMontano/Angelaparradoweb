import http.server, socketserver, sys, os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8504
FILE = sys.argv[2] if len(sys.argv) > 2 else "index.html"
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "/" + FILE
        return super().do_GET()
    def log_message(self, *a): pass

with socketserver.TCPServer(("", PORT), H) as s:
    s.serve_forever()
