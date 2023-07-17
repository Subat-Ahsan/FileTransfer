# FileTransfer

A simple program that allows the user to host a server on one computer and get files  
from the server to a client running on a different computer. 

## Usage
Run server.py on the machine containing the files. Make sure  
the files are contained in the 'files' folder in the same directory as the server script. 

Run the client script on the computer requesting the file. Input the name of the file, the destination  
file it should be saved to, the address of the server and the port it is on (7190 by default).

```
C:\Your\Directory>python client.py
What is the filename: filename.mp4
What is the destination file: output_file.mp4
What is the host: [Public or Private IPv4 address]
What is the port: 7190
Size:  325670587
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75  
76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 
Done

```

If port forwarding is enabled for the computer running server.py, the public ip of the 
network can be used by the client.  
Enter the IPv4 of the server computer if client and server are on the same network.  
Enter the public IP
of the network on which server.py is running if they are not.  