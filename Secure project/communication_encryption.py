import socket
import ssl

class CommunicationEncryption:
    def __init__(self, certfile, keyfile):
        self.certfile = certfile
        self.keyfile = keyfile

    def create_secure_socket(self):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        secure_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_side=True)
        return secure_socket
