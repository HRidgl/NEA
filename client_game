### This file is used to create the server computer and handle the socket connections of clients.

# Importing modules
from main import *
from player import *

# Class used to make a computer turn into a server
class Server:

    # Array for all the clients to enable broadcasting
    Clients = []

    def __init__(self):
        self.HEADER = 64  # First message to the server is 64 bytes
        self.PORT = 5050  # Port location
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
        self.ADDR = (self.SERVER, self.PORT)  # Makes a tuple
        self.FORMAT = 'utf-8' # Declares the encoding format
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address

        self.server.bind(self.ADDR) # Binding the address and port to form a socket
    

    # Handles individual connections between client and server
    def handle_client(self, conn, addr):
        connected = True

        print(f"New connection {addr} connected.")
        self.send_message('THIS CLIENT IS NOW CONNECTED',conn)

        while connected == True:

            self.total_clients()

            header = conn.recv(self.HEADER)
            if not header:
                print(f"[DISCONNECTED] {addr} disconnected.")
                break
            
            data = self.receive_objects(conn,header)

            print("Received object:", data)
            print(f"Player position: ({data.x}, {data.y})")

            self.broadcast((data.x,data.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        conn.close()


    # Method to broadcast messages to all clients
    def broadcast(self,message):
        for client in self.Clients:
            self.send_message(message,client)


    # Method to send a message to a single client
    def send_message(self,object,conn):
        data = pickle.dumps(object)
        data_length = len(data)
        header = f"{data_length:<{self.HEADER}}".encode(self.FORMAT)
        conn.sendall(header + data)


    # Method used to receive objects from clients
    def receive_objects(self,conn,header):
        data_length = int(header.decode(self.FORMAT).strip())
        data = conn.recv(data_length)
        data = pickle.loads(data)
        return data
    

    # Method used to broadcast the current number of active clients
    def total_clients(self):
        total = 0
        for client in self.Clients:
            total +=1
        self.broadcast(f"There are currently {total} clients")


    # Initiates the client server connection set up
    def start(self):
        self.server.listen(2)  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            self.Clients.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
            
s = Server()
s.start()
