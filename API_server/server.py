import http.server
import socketserver

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/test':
            self.path = 'test.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8004
handler = myhandler

myserver = socketserver.TCPServer(("localhost",PORT),handler)
myserver.serve_forever()
