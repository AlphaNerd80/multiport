from threading import Thread
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello World!")

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def serve_on_port(port):
    server = ThreadingHTTPServer(("localhost",port), Handler)
    server.serve_forever()


port1 = 1111
port2 = 2222
Thread(target=serve_on_port, args=[port1]).start()
serve_on_port(port2)