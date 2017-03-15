#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json

class SampHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/post":
            self.send_error(404)

        text = self.rfile.read(int(self.headers['Content-Length'])).decode()
        stuff = json.loads(text)
        print(stuff)

        '''
        c = sqlite3.connect("blog.db").cursor()
        query = "INSERT INTO posts (title,body) VALUES ?,?;"
        c.execute(query, (title, body))
        c.close()
        '''

        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path != "/posts":
            self.send_error(404)

        c = sqlite3.connect("blog.db").cursor()
        c.row_factory = sqlite3.Row
        query = "SELECT post_id,title,body FROM posts;"
        posts = [dict(zip(row.keys(), row)) for row in c.execute(query)]
        c.close()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(posts).encode())

def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SampHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
