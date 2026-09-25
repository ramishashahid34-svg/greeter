from http.server import HTTPServer, BaseHTTPRequestHandler

NAME = "Ramisha"

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            f"<h1>Hi, {NAME}!</h1>"
            "<p>Today is a great day to ship code.</p>".encode()
        )

server = HTTPServer(("localhost", 5000), GreeterHandler)

print("Server running at http://localhost:5000")
server.serve_forever()