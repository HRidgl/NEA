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
        self.client.connect(self.ADDR) #Connecting the client to the server

        self.players = [] #Making an array to store the players
        self.player1 = Player(100,100,50,50) # Creating player object
        self.players.append(self.player1) # Adding the player to the players array


    # Method for sending the object to the server computer using pickle sterilisation and sockets
    def send_object(self, obj):
        serialized_data = pickle.dumps(obj)
        data_length = len(serialized_data)
        header = f"{data_length:<{self.HEADER}}".encode(self.FORMAT)
        self.client.sendall(header + serialized_data)


    # Method for receiving objects from the server
    def receive_message(self):
        header = self.client.recv(self.HEADER).decode(self.FORMAT)
        if header != '':
            header = header.strip()
            data_length = int(header)
            serialized_data = self.client.recv(data_length)
            data = pickle.loads(serialized_data)
            return data
