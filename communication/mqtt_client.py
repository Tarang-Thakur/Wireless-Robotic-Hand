import socket


class TCPClient:

    def __init__(self):

        self.server_host = "3.239.60.127"
        self.server_port = 5000

        self.client_id = "laptop"
        self.target_id = "espB"

        self.sock = None
        self.connected = False

    def connect(self):

        try:

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.server_host, self.server_port))

            hello = f"ID:{self.client_id}|TO:*|MSG:HELLO\n"
            self.sock.sendall(hello.encode())

            self.connected = True
            print("[Laptop] Connected to server")

        except Exception as e:

            self.connected = False
            print("[Laptop] Connection failed")

    def send_servos(self, servos):

        if not self.connected:
            return

        try:

            values = [
                servos["thumb"],
                servos["index"],
                servos["middle"],
                servos["ring"],
                servos["pinky"]
            ]

            value_str = ",".join(map(str, values))

            packet = f"ID:{self.client_id}|TO:{self.target_id}|MSG:SERVOS={value_str}\n"

            self.sock.sendall(packet.encode())

        except:

            self.connected = False