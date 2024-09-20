import socket

# Constants
HEADER = 64  #First message to the server is 64 bytes
PORT = 5050  #port location
SERVER = '172.20.63.213'
ADDR = (SERVER, PORT)  #makes a tupple
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "! DISCONNECTED"

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)  # Create socket family/type
client.connect(ADDR)


def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))  # Padding up to 64 bytes
  client.send(send_length)
  client.send(message)
  print(client.recv(2048).decode(FORMAT))

msg = ''
while msg != 'STOP':
  msg = input("Enter a message: ").upper()
  if msg == 'STOP':
    send(DISCONNECT_MESSAGE)
  else:
    send(msg)
