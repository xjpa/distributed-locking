from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

counter = 0
counter_lock = threading.Lock()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        if self.path == "/increment":
            with counter_lock:
                counter += 1
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(counter).encode())
        elif self.path == "/value":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str(counter).encode())
        elif self.path == "/current":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str(counter).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Running server on port 8000...")
    httpd.serve_forever()
