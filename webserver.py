import http.server
import socketserver

PORT = 8080
DIRECTORY = "gui"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def startServer():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()