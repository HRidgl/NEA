### This file is used as a server to handle all the client connections

# Importing all the modules from the main
from main import *

# Class used for making my server
class Server:

    # Instantiation
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECTED"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.ADDR)
        self.clients = []


    # Used as the main loop to receive incoming data from each client
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        self.clients.append(conn)
        connected = True
        while connected:
            try:
                header = conn.recv(self.HEADER).decode(self.FORMAT).strip()
                if header:
                    data_length = int(header)
                    serialized_data = conn.recv(data_length)
                    player_data = pickle.loads(serialized_data)
                    self.broadcast_to_others(player_data, conn)
            except Exception as e:
                print(f"Error handling client {addr}: {e}")
                connected = False
                break
        conn.close()
        self.clients.remove(conn)
        print(f"[DISCONNECTED] {addr} disconnected.")


    # Broadcast player data to all other clients except the sender
    def broadcast_to_others(self, player_data, sender_conn):
        message = pickle.dumps((player_data.x, player_data.y))
        header = f"{len(message):<{self.HEADER}}".encode(self.FORMAT)
        for client in self.clients:
            if client != sender_conn:
                try:
                    client.sendall(header + message)
                except:
                    self.clients.remove(client)


    # Used to listen for clients. Once they are noticed, a socket is created and a thread is ran.
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

#------------------------------------------------------- MAIN -------------------------------------------------------#

# Start the server
s = Server()
s.start()
