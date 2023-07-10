import socket

filename = input("What is the filename: ")
dest = input("What is the destination file: ")
host = input("What is the host: ")

try:
    port = int(input("What is the port: "))
except:
    print("Invalid")
    exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
s.send(filename.encode())
message = s.recv(1024).decode()
if message == "!NOTFOUND":
    print("Not found")
else:
    f = open(dest, 'wb')
    while True:
        x = s.recv(1024)
        if not x:
            print("Done")
            break
        f.write(x)
