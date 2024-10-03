# Importing all modules from the main
from main import *
from player import *

# Class used to handle client requests and connects the client to the server
class Client:
    
    def __init__(self):
        self.HEADER = 64  #First message to the server is 64 bytes
        self.PORT = 5050  #port location
        self.SERVER = '172.20.53.216' # fill with server ip
        self.ADDR = (self.SERVER, self.PORT)  #makes a tuple
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.client = socket.socket(socket.AF_INET,
                            socket.SOCK_STREAM)  # Create socket family/type
        self.client.connect(self.ADDR)

        # Example object to send
        #self.data = {'name': 'Holly', 'age': 17, 'city': 'Notts'}
        self.data = Player(100,100,50,50)


    # Sending a message to the server
    def send(self,msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))  # Padding up to 64 bytes
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(self.FORMAT))

    def send_object(self):
       # Serialize the object
        serialized_data = pickle.dumps(self.data)

        # Send the serialized object
        self.client.sendall(serialized_data)
        
        self.client.close()

#---------------------------------MAIN---------------------------------#
#p = 

c = Client()

c.send_object()

###################################################################################
