### This file is used to handle all the clients' interractions with the server

# Importing all the modules from the main
from main import *

# Importing the player class from another file
from player import *

# This class is used to handle client-server interractions
class Client:

    # Instantiation
    def __init__(self,player):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = '192.168.1.171'  # Replace with actual server IP
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECTED"

        self.player = player

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.player1 = Player("Player 1", 100, 100, 50, 50, (255,0,0))
        self.player2 = Player("Player 2", 200, 200, 50, 50, (0, 0, 255))


    # Method used to send objects to the server
    def send_object(self, obj):
        serialized_data = pickle.dumps(obj)
        header = f"{len(serialized_data):<{self.HEADER}}".encode(self.FORMAT)
        self.client.sendall(header + serialized_data)


    # Method used to receive objects from the server
    def receive_data(self):
        while True:
            try:
                header = self.client.recv(self.HEADER).decode(self.FORMAT).strip()
                if header:
                    data_length = int(header)
                    serialized_data = self.client.recv(data_length)
                    data = pickle.loads(serialized_data)
                    self.process_received_data(data)
            except Exception as e:
                print(f"Error receiving data: {e}")
                break


    # Method used to smooth the movement of the other player using interpolation
    def process_received_data(self, data):
        if isinstance(data, tuple) and len(data) == 2:
            if self.player == 1:
                self.player2.x += (data[0] - self.player2.x) * 0.1
                self.player2.y += (data[1] - self.player2.y) * 0.1
            else:
                self.player1.x += (data[0] - self.player1.x) * 0.1
                self.player1.y += (data[1] - self.player1.y) * 0.1
