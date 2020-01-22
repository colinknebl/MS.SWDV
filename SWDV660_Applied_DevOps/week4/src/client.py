import socket
import sys

from server import Server

class Client:
    def __init__(self):
        self.socket = socket.socket()
        self.host = socket.gethostname()

    def connect(self, port):
        self.socket.connect((self.host, port))

    def close(self):
        self.socket.close()

    def send(self, string):
        self.socket.sendall(string.encode())
        data = self.socket.recv(1024)
        return data.decode()


if __name__ == '__main__':
    # get the message to send to the server
    # if no message is supplied to the script 'Hello' is sent
    MESSAGE = sys.argv[1] if len(sys.argv) > 1 else 'Hello'

    # initialize the client
    client = Client()

    # connect to the server
    client.connect(Server.port)

    # print the message that is going to be sent to the server
    print('Sending message to server: "{}"'.format(MESSAGE))

    # send the message to the server
    response = client.send(MESSAGE)

    # print the response from the server
    print('Server response = {}'.format(response))
    
    # close the connection
    client.close()
