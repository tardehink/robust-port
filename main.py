import socket

class RobustPort:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        try:
            self.socket.connect((host, port))
            print(f'Connected to {host}:{port}')
        except Exception as e:
            print(f'Failed to connect: {e}')

if __name__ == '__main__':
    rp = RobustPort()
    rp.connect('localhost', 8080)
