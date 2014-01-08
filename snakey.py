import logging
import socket, SocketServer
from contextlib import contextmanager
log = logging.getLogger('snake_in_the_middle')
log.setLevel(logging.DEBUG)
log.addHandler(logging.FileHandler('activity.log'))

class SnakeInTheMiddle(SocketServer.ThreadingMixin, 
                       SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        log.debug(self.data)
        self.request.sendall(self.data.upper())


@contextmanager
def socket_client(ip='127.0.0.1', port=42000):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        yield sock
    finally:
        sock.close()


def main():
    with socket_client() as c:
        c.send('hello')
        log.debug(s.recv(1024))
        log.debug("hai")


if __name__ == "__main__":
    main()
