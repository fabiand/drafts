#!/usr/bin/env python3

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pprint import pprint

if len(sys.argv)-1 != 2:
    print("Usage: {} <port_number> <url>".format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        print("CON")
        print(self.path, self.headers)
        self.send_response(307)  # 3ß7, temp, 302, perm
        self.send_header('Location', sys.argv[2] + self.path)
        self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
