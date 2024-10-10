# Importing all modules from the main
from main import *
import socket
import pickle
from player import *

# Class used to handle client requests and connects the client to the server
class Client:
    
    def __init__(self):
        self.HEADER = 64  #First message to the server is 64 bytes
        self.PORT = 5050  #port location
        self.SERVER = '172.20.52.237' #server ip
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
    def send_object(self,object):
       # Serialize the object
        serialized_data = pickle.dumps(object)

        # Send the serialized object
        self.client.sendall(serialized_data)

#---------------------------------MAIN---------------------------------#
c = Client()
c.send_object(c.player1)
