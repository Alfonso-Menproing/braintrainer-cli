import socket

class ComunicatorClient:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 1029
    def send(self, command):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.send(command)
        recv_info = self.sock.recv(1024)
        self.sock.close()
        return recv_info
def main():
    cc = ComunicatorClient()
    is_done = False
    while not is_done:
        try:
            data = raw_input()
            print(cc.send(data))
        except EOFError:
            is_done = True

if __name__ == "__main__":
    main()

