import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_time(self):
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        json_string =json.dumps({'now':str(datetime.now())})

        # solution 1
        self.wfile.write(bytes(json_string,'utf-8')) 

    def do_GET(self):
        request_path = self.path
        if request_path == '/time':
            self.do_time()
        #self.send_response(200)
        #self.send_header("Set-Cookie", "foo=bar")
        #self.end_headers()
        #json_string =json.dumps({'now':str(datetime.now())})
        
        # solution 1
        #self.wfile.write(bytes(json_string,'utf-8'))
        
      
    def do_POST(self):
        request_path = self.path


        request_headers = self.headers
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        json_string =json.dumps({'now':str(datetime.now())})
        self.wfile.write(bytes(json_string,'utf-8'))

def main():
    port = 9004
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
