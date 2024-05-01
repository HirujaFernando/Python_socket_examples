# Anyone in the same LAN which are connected to the same router as the server can connect with it in this example

import socket
import threading

HEADER = 64 # Maximum length of header. In this case is 64 bytes
PORT = 5050 # Important: set a port that isn't used normally by the computer. Can't use ports such as 8080 or 8000
SERVER = socket.gethostbyname(socket.gethostname()) # Get computer(server) IP address(IPV4) 
ADDR = (SERVER, PORT) # A tuple is used to bind the the server to the network
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"

# Make connection by selecting the type of family(category) and method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # Bind the server to network

# Runs concurrently for all clients
def handle_client(conn, addr):
    print(f"NEW CONNECTION WITH: {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # Wait until client sends a message and decode message from bytes using utf-8
        if msg_length: # Check whether message is valid
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{addr}: {msg}")
            conn.send("Message received!".encode(FORMAT)) # Send messages to client
    
    conn.close() # Close connection properly

# Start making connections
def start():
    server.listen()
    print(f"Server listening at {SERVER}")
    while True:
        conn, addr = server.accept() # Wait until client accepts
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Start new thread for the new client
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")

print("SERVER IS STARTING...")
start()