# Importing all modules from the main
from main import *
from player import *

# Class used to handle client requests and connects the client to the server
class Client:
    
    def __init__(self):
        self.HEADER = 64  #First message to the server is 64 bytes
        self.PORT = 5050  #port location
        self.SERVER = '172.20.53.198' # fill with server ip
        self.ADDR = (self.SERVER, self.PORT)  #makes a tuple
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Create socket family/type
        self.client.connect(self.ADDR)

        self.players = []

        # Objects to send
        self.player1 = Player(100,100,50,50)
        self.players.append(self.player1)

    def send_object(self,object):
       # Serialize the object
        serialized_data = pickle.dumps(object)

        # Send the serialized object
        self.client.sendall(serialized_data)

        self.client.close()

#---------------------------------MAIN---------------------------------#
c = Client()
c.send_object(c.player1)
