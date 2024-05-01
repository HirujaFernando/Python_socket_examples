# video tutorial: https://www.youtube.com/watch?v=3QiPPX-KeSc
# time: 36:32

import socket

HEADER = 64 # Maximum length of header. In this case is 64 bytes
PORT = 5050 # Same port as server
SERVER = socket.gethostbyname(socket.gethostname()) # Get computer(server) IP address(IPV4) 
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# send messages
def send(msg):
    message = msg.encode(FORMAT) # convert into a bytes format
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length)) # pad the message with blank spaces represented in bytes to suit HEADER
    client.send(send_length) # send length of message
    client.send(message) # send actual message
    print(client.recv(2048).decode(FORMAT)) # enable the client to receive messages from server

send("Hello server!")

while True:
    user = input("Send: ")
    if user == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        break
    else:
        send(user)