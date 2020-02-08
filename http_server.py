from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
import sys
import traceback

feature_result = '{"usd_txn_fp_6hr":"0.1"}'


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode(encoding='utf_8'))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

            # refuse to receive non-json content
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                return

            # read the message and convert it into a python dictionary
            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            entity_id = int(message['entity_id'])

            if entity_id % 10 > 5:
                self.send_response(400)
                self.end_headers()
            else:
                # send the message back
                self._set_headers()
                self.wfile.write(feature_result.encode(encoding='utf_8'))
        except Exception:
            traceback.print_exc(file=sys.stdout)
            self.send_response(400)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)

    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


