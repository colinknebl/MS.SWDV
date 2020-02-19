from Crypto.Cipher import AES
from Crypto import Random

class Cipher:
    def __init__(self, key):
        self.key = key
        self.AES = AES.new(key, AES.MODE_CFB, 'iv_0123412341234') # Random.new().read(16)

    def encrypt(self, plainText):
        return self.AES.encrypt(plainText)

    def decrypt(self, cipherText):
        return self.AES.decrypt(cipherText)
