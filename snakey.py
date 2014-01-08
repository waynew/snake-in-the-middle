import logging
import thread
import socket, SocketServer
from contextlib import contextmanager
log = logging.getLogger('snake_in_the_middle')
log.setLevel(logging.DEBUG)
log.addHandler(logging.FileHandler('activity.log'))
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)

INBOUND_IP = '127.0.0.1'
INBOUND_PORT = 42000
OUTBOUND_IP = '127.0.0.1'
OUTBOUND_PORT = 42001

log.info("^C to quit")
try:
    log.debug('Creating inbound socket')
    in_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log.debug('Binding listner to %s:%s ...', INBOUND_IP, INBOUND_PORT)
    in_sock.bind((INBOUND_IP, INBOUND_PORT))
    in_sock.listen(5)
    log.debug('OK')
    while True:
        log.debug('Creating outbound socket')
        out_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.debug('Connecting outbound to %s:%s ...',
                  OUTBOUND_IP, OUTBOUND_PORT)
        out_sock.connect((OUTBOUND_IP, OUTBOUND_PORT))
        log.debug('OK')
        log.debug('Waiting for connection...')
        client, addr = in_sock.accept()
        log.debug('Connected to %s:%s', *addr)
        data = 'stuff goes here'
        while data.strip(): #contains non-whitespace
            data = client.recv(1024)
            log.debug('Data:')
            log.debug(data)
            log.debug('End data')
            out_sock.sendall(data)
            client.sendall(out_sock.recv(1024))
        log.debug('Closing client connection ...')
        client.close()
        log.debug('OK')
        out_sock.close()
except KeyboardInterrupt:
    log.info("^C caught, shutting down...")
except:
    log.exception("Something happened")
    raise
finally:
    if client: client.close()
    in_sock.close()
    out_sock.close()
    log.info("Bye.")
