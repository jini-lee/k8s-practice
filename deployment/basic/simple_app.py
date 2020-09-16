#!/usr/bin/env python3

import http.server


class SimpleWebServer(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header('Content-Type', 'text/html')
        s.end_headers()
        s.wfile.write(b'''
<!DOCTYPE html>
<html>
    <head>
        <title>PYTHON SIMPLE V1!</title>
    </head>
    <body>
        <p>This is a simple app V1!</p>
    </body>
</html>''')


if __name__ == '__main__':
    httpd = http.server.HTTPServer(('0.0.0.0', 8080), SimpleWebServer)
    httpd.serve_forever()
