import socket
from contextlib import contextmanager

@contextmanager
def open_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', 42000))
        yield
    except:
        sock.close()

@contextmanager
def run():
    with open_socket():
        yield
