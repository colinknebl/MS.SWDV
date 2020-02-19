import sys
from CA import CA
from server import Server
from client import Client

def main():
    # get the message to send to the server
    # if no message is supplied to the script 'Hello' is sent
    MESSAGE = sys.argv[1] if len(sys.argv) > 1 else 'Hello'

    # initialize the Certificate Authority
    ca = CA()

    # register the server with the CA
    ca.register(Server.name, Server.publicKey)

    # The client will initiate contact with the server
    # initialize the client
    client = Client(ca, Server.port)

    # # send the message to the server
    response = client.send(MESSAGE)

    # # print the response from the server
    print('Server response = {}'.format(response))


if __name__ == '__main__':
    main()