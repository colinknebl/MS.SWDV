import socket
from cipher import Cipher

class Server:
    name = 'Server1'
    publicKey = 'public_key123456'
    port = 9500

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.socket.bind((host, Server.port))
        self.cipher = Cipher(Server.publicKey)

    def __del__(self):
        self._close()

    def __decrypt(self, cipherText):
        return self.cipher.decrypt(cipherText)

    def listen(self):
        self.socket.listen(5)
        conn, addr = self.socket.accept()
        print( 'Connected by {}'.format(addr))

        # send server name
        conn.send(Server.name)

        # receive session cipher key
        encryptedSessionCipherKey = conn.recv(1024)
        sessionCipherKey = self.__decrypt(encryptedSessionCipherKey)

        if sessionCipherKey == 'session cipher key':
            conn.send(self.cipher.encrypt('session cipher key acknowledged'))
        else: 
            conn.send('Goodbye')
            conn.close()

        while True:
            encryptedData = conn.recv(1024)
            if not encryptedData: break
            decryptedData = self.__decrypt(encryptedData)
            if decryptedData == b'Hello':
                conn.send(self.cipher.encrypt('Hi'))
            else:
                conn.send(self.cipher.encrypt('Goodbye'))

        conn.close()
        # self.listen()

    def _close(self):
        self.socket.close()

        
if __name__ == '__main__':
    server = Server()
    server.listen()
