import socket, time, threading

LOADING_BARS = 101
LOAD_REFRESH_RATE = 0.01
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

def load(data):
    print("Size: ", data['size'])
    current_load = 0

    while True:
        amount = data['current_size'] / data['size'] 
        new_load = int(LOADING_BARS * amount)
        
        if new_load > current_load:
            for i in range(current_load, new_load):
                print(i, end=' ', flush=True)
            current_load = new_load
        
        if amount >= 1:
            break
        time.sleep(0.1)
    
if message == "!NOTFOUND":
    print("Not found")

else:
    
    data = {'size': int(message.split(',')[1]), 'current_size': 0, 'finished': False}
    t = threading.Thread(target=load, args=(data,))
    t.start()
    f = open(dest, 'wb')
    while True:
        x = s.recv(1024)
        data["current_size"] += 1024
        if not x:
            data['finished'] = True
            break
        f.write(x)
    t.join()
    print("\nDone")

