import http.server
import socketserver
import json
import os, sys

from parser import parse, create_classifier

PORT = 8081


class Handler(http.server.BaseHTTPRequestHandler):
    use_old = os.path.exists("clf.pickle") and (len(sys.argv) == 1 or sys.argv[1] != "-t")
    clf, nrows, ncols = create_classifier(use_old)

    def add_headers(self):
        self.send_header("Content-type", "text/json")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:8000")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
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
    HOST, PORT = "localhost", 8081
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), Handler)
    try:
        print("Serving at: http://{}:{}".format(HOST, PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down")
        server.shutdown()