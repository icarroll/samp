#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class SampHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/post":
            self.send_error(404, "No such endpoint")

        print("doing POST", self.requestline, self.command, self.path)

    def do_GET(self):
        if self.path != "/posts":
            self.send_error(404, "No such endpoint")

        print("doing GET", self.requestline, self.command, self.path)

def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SampHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
