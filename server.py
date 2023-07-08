import socket
from const import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()

while True:
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    message = conn.recv(MAX_SIZE).decode(FORMAT)
    conn.send(f"Recieved {message}".encode(FORMAT))
    conn.close()
