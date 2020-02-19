import socket
import sys

from server import Server
from cipher import Cipher

class Client:
    def __init__(self, certAuthority, port):
        self.certAuthority = certAuthority
        self.host = socket.gethostname()
        self.serverPort = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.__close()
    
    def __validateServerName(self, serverName):
        return self.certAuthority.validate(serverName)

    def __establishConnection(self):
        self.socket.connect((self.host, self.serverPort))
        serverName = self.socket.recv(1024)
        return self.__validateServerName(serverName)

    def __getSessionKey(self, cipher):
        encryptedSessionKey = cipher.encrypt('session cipher key')
        return encryptedSessionKey

    def send(self, msg):
        serverKey = self.__establishConnection()
        cipher = Cipher(serverKey)

        if serverKey is None:
            self.socket.send('Goodbye')
            return self.__close()
        else:
            encryptedSessionKey = self.__getSessionKey(cipher)
            self.socket.send(encryptedSessionKey)
            encryptedData = self.socket.recv(1024)
            decryptedData = cipher.decrypt(encryptedData)
            if decryptedData != 'session cipher key acknowledged':
                self.socket.send('Goodbye')
                return self.__close()
        
        print('Client/Server acknowledgement successful!')

        encryptedMsg = cipher.encrypt(msg)
        self.socket.send(encryptedMsg)

        encryptedData = self.socket.recv(1024)
        decryptedData = cipher.decrypt(encryptedData)

        self.__close()
        return decryptedData

    def __close(self):
        self.socket.close()
