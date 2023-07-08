import socket
from const import *


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT)) 

client.send("HELLO".encode(FORMAT))
print(client.recv(MAX_SIZE).decode(FORMAT))