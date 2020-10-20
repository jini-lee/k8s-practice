#!/usr/bin/env python3

import http.server
import sys

requested_cnt = 0
class SimpleWebServer(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        global requested_cnt
        requested_cnt += 1
        sys.stderr.write('Error, echo with no symbols!')
        sys.stdout.flush()
        s.send_response(200)
        s.send_header('Content-Type', 'text/html')
        s.end_headers()
        s.wfile.write(b'''
<!DOCTYPE html>
<html>
    <head>
        <title>PYTHON SIMPLE PAGE!</title>
    </head>
    <body>
        <p>This is a simple page!</p>
    </body>
</html>''')


if __name__ == '__main__':
    httpd = http.server.HTTPServer(('0.0.0.0', 8080), SimpleWebServer)
    httpd.serve_forever()
