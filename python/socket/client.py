import socket

if __name__ == '__main__':
    target_server = ('localhost', 5000)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _socket:
        _socket.connect(target_server)
        _socket.send(b'Hello world.')
        response = _socket.recv(1024)
        print(response)
