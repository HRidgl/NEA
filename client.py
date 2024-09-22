# Importing all modules from the main
from main import *

# Class used to handle client requests and connects the client to the server
class Client:
    
    def __init__(self):
        self.HEADER = 64  #First message to the server is 64 bytes
        self.PORT = 5050  #port location
        self.SERVER = '172.20.63.213' # fill with server ip
        self.ADDR = (self.SERVER, self.PORT)  #makes a tuple
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.client = socket.socket(socket.AF_INET,
                            socket.SOCK_STREAM)  # Create socket family/type
        self.client.connect(self.ADDR)


    # Sending a message to the server
    def send(self,msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))  # Padding up to 64 bytes
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(self.FORMAT))

#---------------------------------MAIN---------------------------------#
c = Client()

# Keeps asking the client for a message until they send 'STOP'
msg = ''
while msg != 'STOP':
  msg = input("Enter a message: ").upper()
  if msg == 'STOP':
    c.send(c.DISCONNECT_MESSAGE)
    print("This client is now disconnected")
  else:
    c.send(msg)
