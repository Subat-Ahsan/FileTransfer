import socket
import os

LOCAL_HOST = socket.gethostbyname(socket.gethostname())
PORT = 7190
MAX_SIZE = 1024
FORMAT = 'utf-8'
DIR = 'files'

if not os.path.isdir(DIR):
    os.mkdir(DIR)

import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((LOCAL_HOST,PORT))



while True:
    server.listen()
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    filename = conn.recv(MAX_SIZE).decode()
    if filename in os.listdir(DIR):
        conn.send(f"FOUND,{os.path.getsize(os.path.join(DIR,filename))}".encode())
        f = open(os.path.join(DIR,filename),'rb')
        while True:
            x = f.read(1024)
            conn.send(x)
            if not x:
                print('Done')
                break
        f.close
    else:
        conn.send("!NOTFOUND".encode())

    conn.close()
    
