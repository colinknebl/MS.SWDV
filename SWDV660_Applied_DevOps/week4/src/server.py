import socket

class Server:
    port = 9500

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.socket.bind((host, Server.port))

    def __del__(self):
        self._close()

    def _send(self, conn, string):
        conn.sendall(string.encode())

    def _accept(self):
        conn, addr = self.socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data == b'Hello':
                    self._send(conn, 'Hi')
                else:
                    self._send(conn, 'Goodbye')
                    self.listen(False)

    def listen(self, printmsg=True):
        self.socket.listen(5)
        if printmsg:
            print('Server listening on port: {}'.format(Server.port))
        self._accept()

    def _close(self):
        self.socket.close()

        
if __name__ == '__main__':
    server = Server()
    server.listen()
