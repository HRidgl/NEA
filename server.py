### This file is used to create the server computer and handle the socket connections of clients.

# Importing modules
from main import *
from player import *

# Class used to make a computer turn into a server
class Server:

    Clients = []

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

        self.send_message('THIS CLIENT IS NOW CONNECTED',conn)

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

                total = 0

                for i in self.Clients:
                    total +=1

                self.broadcast(total)
                #self.send_message(player,conn)

                #print("Received object:", player)
                #print(f"Player position: ({player.x}, {player.y})")

                # Checking if the quit button has been pressed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            except Exception as e:
                print(f"[ERROR] {e}")
                connected = False

        conn.close()


    def broadcast(self,message):
        for client in self.Clients:
            self.send_message(message,client)


    def send_message(self,message,conn):
        data = pickle.dumps(message)
        data_length = len(data)
        header = f"{data_length:<{self.HEADER}}".encode(self.FORMAT)
        conn.sendall(header + data)


    # Initiates the client server connection set up
    def start(self):
        self.server.listen(5)  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            self.Clients.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
            
s = Server()
s.start()
