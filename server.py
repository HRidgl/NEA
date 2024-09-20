# Importing modules
import socket
import threading

# Constants
HEADER = 64  # First message to the server is 64 bytes
PORT = 5050  # port location
SERVER = socket.gethostbyname(socket.gethostname())  # Gets the IPv4
ADDR = (SERVER, PORT)  # makes a tupple
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "! DISCONNECTED"

print(SERVER)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket family/type
server.bind(ADDR)  # Binds the 2 items together in the tupple address


# Handles individual connections between client and server
def handle_client(conn, addr):
    print(f"New connection {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # Wait until something is sent over the socket
        if msg_length:
            msg_length = int(msg_length)  # Shows length of the message that is about to be recieved
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] This client is now disconnected")

            else:
                print(f"[{addr}]{msg}")
                server_msg = input("--> ").upper()
                conn.send(server_msg.encode(FORMAT))

    conn.close()


# Initiates the client server connection set up
def start():
    server.listen()  # Waits for connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # Shows how many connections there are


######################### MAIN #########################
print("Server is starting... ")
start()
