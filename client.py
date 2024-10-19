# Importing all modules from the main
from main import *
from player import *

# Class used to handle client requests and connects the client to the server
class Client:
    
    def __init__(self):
        self.HEADER = 64  #First message to the server is 64 bytes
        self.PORT = 5050  #port location
        self.SERVER = '192.168.1.171' #server ip
        self.ADDR = (self.SERVER, self.PORT)  #makes a tuple
        self.FORMAT = 'utf-8' #format to encode and decode data
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Create socket family/type
                
        self.client.connect(self.ADDR)

        self.players = [] #Making an array to store the players

        # Object to send
        self.player1 = Player(100,100,50,50)
        self.players.append(self.player1)


    # Sending the object to the server computer
    def send_object(self, obj):
        # Serialize the object
        serialized_data = pickle.dumps(obj)

        # Get the length of the serialized data
        data_length = len(serialized_data)

        # Create a fixed-size header with the length of the data (64 bytes)
        header = f"{data_length:<{self.HEADER}}".encode(self.FORMAT)

        # Send the header and the serialized object
        self.client.sendall(header + serialized_data)


    def receive_message(self):
        try:
            header = self.client.recv(self.HEADER).decode(self.FORMAT)
            if header:
                data_length = int(header.strip())
                serialized_data = self.client.recv(data_length)
                data = pickle.loads(serialized_data)
                print(data)
            
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None


    def disconnect(self):
        self.send_object(self.DISCONNECT_MESSAGE)
        self.client.close()
