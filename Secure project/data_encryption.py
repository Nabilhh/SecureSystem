from Crypto.Cipher import AES
import base64

class DataEncryption:
    def __init__(self, key):
        self.key = key[:32].encode('utf-8')
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self, plaintext):
        nonce = self.cipher.nonce
        ciphertext, tag = self.cipher.encrypt_and_digest(plaintext.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        decoded = base64.b64decode(ciphertext)
        nonce = decoded[:16]
        ciphertext = decoded[16:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')
