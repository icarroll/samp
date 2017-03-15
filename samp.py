#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3

class SampHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/post":
            self.send_error(404)

        print("doing POST", self.requestline, self.command, self.path)

    def do_GET(self):
        if self.path != "/posts":
            self.send_error(404)

        c = sqlite3.connect("blog.db").cursor()
        c.execute("SELECT post_id,title,body FROM posts;")
        posts = c.fetchall()
        c.close()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(posts).encode())

def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SampHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
