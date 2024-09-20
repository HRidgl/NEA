# Importing modules
from main import *

class Server:

    def __init__(self):
        self.HEADER = 64  # First message to the server is 64 bytes
        self.PORT = 5050  # port location
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
        self.ADDR = (self.SERVER, self.PORT)  # makes a tupple
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
        self.server.bind(self.ADDR)  # Binds the 2 items together in the tupple address


    # Handles individual connections between client and server
    def handle_client(self, conn, addr):
        print(f"New connection {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)  # Wait until something is sent over the socket
            if msg_length:
                msg_length = int(msg_length)  # Shows length of the message that is about to be recieved
                msg = conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] This client is now disconnected")

                else:
                    print(f"[{addr}]{msg}")
                    server_msg = input("--> ").upper()
                    conn.send(server_msg.encode(self.FORMAT))

        conn.close()


    # Initiates the client server connection set up
    def start(self):
        self.server.listen()  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=s.handle_client(conn,addr))
            thread.start()

            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # Shows how many connections there are


######################### MAIN #########################
print("Server is starting... ")
s = Server()
s.start()
