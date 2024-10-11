### This file is used to create the server computer and handle the socket connections of clients.

# Importing modules
from main import *
from player import *
#from server_game import *

# Class used to make a computer turn into a server
class Server:

    def __init__(self):
        self.HEADER = 64  # First message to the server is 64 bytes
        self.PORT = 5050  # port location
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
        self.ADDR = (self.SERVER, self.PORT)  # makes a tuple
        self.FORMAT = 'utf-8' 
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
        self.server.bind(self.ADDR)  # Binds the 2 items together in the tuple address


    # Handles individual connections between client and server
    def handle_client(self, conn, addr):
        print(f"New connection {addr} connected.")

        connected = True
        while connected == True:

            # First, receive the header to determine the size of the incoming data
            header = conn.recv(self.HEADER)
            if not header:
                print(f"[DISCONNECTED] {addr} disconnected.")
                break
            
            # Get the size of the incoming data
            data_length = int(header.decode(self.FORMAT).strip())
            data = conn.recv(data_length)

            # Deserialize the data using pickle
            player = pickle.loads(data)
            print("Received object:", player)
            print(f"Player position: ({player.x}, {player.y})")

        conn.close()


    # Initiates the client server connection set up
    def start(self):
        self.server.listen(1)  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

            print(f"[ACTIVE CONNECTIONS] {threading.active_count()}")  # Shows how many connections there are
