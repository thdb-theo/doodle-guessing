import http.server
import socketserver
import json
import os, sys
import ssl

from parser import parse, create_classifier

PORT = 8081


class Handler(http.server.BaseHTTPRequestHandler):
    clf, nrows, ncols = create_classifier()

    def add_headers(self):
        self.send_header("Content-type", "text/json")
        # self.send_header("Access-Control-Allow-Origin", "http://129.242.90.161:5000")
        # self.send_header("Access-Control-Allow-Origin", "https://thdb-theo.github.io")
        self.send_header("Access-Control-Allow-Origin", "doodleguesser.com")
        # self.send_header("Access-Control-Allow-Origin", "*")


        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "content-type")

        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.add_headers()

    def do_POST(self):
        self.send_response(200, "ok")
        self.add_headers()

        content_len = int(self.headers.get("Content-Length"))
        if content_len > 100000:
            self.send_error(403, "Request body too large")
        try:
            post_body = json.loads(json.loads(self.rfile.read(content_len)))
        except TypeError:
            self.send_error(400)
            return
        print("Received POST request")
        print(self.headers)
        digit = parse(post_body, self.clf, self.nrows, self.nrows)
        body = bytes(json.dumps({"item": str(digit)}), encoding="utf-8")

        print("Returning")
        print(body)

        self.wfile.write(body)
        self.wfile.write(b"\n")

    def do_GET(self):
        self.send_response(200, "ok")
        self.add_headers()
        self.wfile.write(b"{\"Hello\": \"World\"}\n")

if __name__ == "__main__":
    # HOST, PORT = "129.242.219.114", 8081
    HOST, PORT = "localhost", 8080
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), Handler)
    # server.socket = ssl.wrap_socket(server.socket, certfile="./cert1.pem", keyfile="./key1.pem", server_side=True)
    try:
        print("Serving at: http://{}:{}".format(HOST, PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down")
        server.shutdown()
