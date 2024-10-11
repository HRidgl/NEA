### This file is used to create the server computer and handle the socket connections of clients.

# Importing modules
from main import *
from player import *
#from server_game import *

# Class used to make a computer turn into a server
class Server:

    def __init__(self):
        self.HEADER = 64  # First message to the server is 64 bytes
        self.PORT = 5050  # port location
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
        self.ADDR = (self.SERVER, self.PORT)  # makes a tuple
        self.FORMAT = 'utf-8' 
        self.DISCONNECT_MESSAGE = "! DISCONNECTED"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
        self.server.bind(self.ADDR)  # Binds the 2 items together in the tuple address


    # Handles individual connections between client and server
    def handle_client(self, conn, addr,g):
        print(f"New connection {addr} connected.")

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

                # Checking if the quit button has been pressed
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                '''
                # Drawing the screen
                g.draw()
                #c.player1.draw_player(g.screen)

                # Updating the screen
                g.update_screen()

                # Clockspeed
                g.clock.tick(80)'''

            except Exception as e:
                print(f"[ERROR] {e}")
                connected = False

        conn.close()


    # Initiates the client server connection set up
    def start(self,g):
        self.server.listen(1)  # Waits for connections
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            '''try:
                print("TRUE 1")
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr, g))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count()}")

                while True:'''
            try:
                print("[WAITING FOR CONNECTIONS]")  # Indicate waiting state
                conn, addr = self.server.accept()
                print(f"[NEW CONNECTION] {addr} connected.")
                thread = threading.Thread(target=self.handle_client, args=(conn, addr, g))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count()}")
            except Exception as e:
                print(f"[ERROR ACCEPTING CONNECTION] {e}")

            '''except Exception as e:
                print(f"[ERROR ACCEPTING CONNECTION] {e}")'''
