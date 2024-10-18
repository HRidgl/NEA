### This file is used to create the server computer and handle the socket connections of clients.

# Importing modules
from main import *
from player import *

# Class used to make a computer turn into a server
class Server:

    clients = []

    def __init__(self):
        self.HEADER = 64  # First message to the server is 64 bytes
        self.PORT = 5050  # port location
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
        self.ADDR = (self.SERVER, self.PORT)  # makes a tuple
        self.FORMAT = 'utf-8' 
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address

        self.server.bind(self.ADDR)
    

    # Handles individual connections between client and server
    def handle_client(self, conn, addr):
        print(f"New connection {addr} connected.")
        client = {'client name': 'bob', 'client socket': conn}

        client_name = client['client name']
        client_socket = client['client socket']

        Server.clients.append(client)

        connected = True
        while connected == True:

            try:
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
                #msg = 'true'
                #self.broadcast_message(client_name,msg)

                # Checking if the quit button has been pressed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            except Exception as e:
                print(f"[ERROR] {e}")
                connected = False

        conn.close()

    def broadcast_message(self,sender_name,msg):
        for client in self.clients:
            client_name = client['client name']
            client_socket = client['client socket']
            message = msg.encode(self.FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.FORMAT)
            send_length += b' ' * (self.HEADER - len(send_length))  # Padding up to 64 bytes
            self.server.send(send_length)
            self.server.send(message)
            #print(self.client.recv(2048).decode(self.FORMAT))
            #if client_name != sender_name:

    # Initiates the client server connection set up
    def start(self):
        self.server.listen(5)  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:  # Indicate waiting state
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()}")
            
s = Server()
s.start()
