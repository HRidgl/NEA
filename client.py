import threading
import time
import socket
import pickle
from player import Player  # Import Player class (assumed to be defined in another file)
import pygame

class Client:
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = '192.168.1.171'  # Replace with actual server IP
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECTED"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.player2 = Player("Player 2", 200, 200, 50, 50, (0, 0, 255))

    def send_object(self, obj):
        serialized_data = pickle.dumps(obj)
        header = f"{len(serialized_data):<{self.HEADER}}".encode(self.FORMAT)
        self.client.sendall(header + serialized_data)

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

    def process_received_data(self, data):
        # Assuming `data` is the position tuple (x, y) for player1.
        if isinstance(data, tuple) and len(data) == 2:
            # Smooth update using interpolation
            self.player2.x += (data[0] - self.player2.x) * 0.1
            self.player2.y += (data[1] - self.player2.y) * 0.1

# Start the receive thread
c = Client()
threading.Thread(target=c.receive_data, daemon=True).start()
