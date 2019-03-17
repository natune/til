import socketserver


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request = self.request.recv(1024)
        print(request)
        self.request.sendall(b'Good Bye.')


class MyServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True


if __name__ == '__main__':
    host = 'localhost'
    port = 5000

    server = MyServer((host, port), RequestHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
