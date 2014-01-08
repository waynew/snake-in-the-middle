import socket
import unittest
import snakey

class TestTheSnake(unittest.TestCase):
    def test_it_should_be_possible_to_connect_to_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with snakey.run():
            sock.connect(('127.0.0.1', 42000))
    

if __name__ == "__main__":
    unittest.main()
