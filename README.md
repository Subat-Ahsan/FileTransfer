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
What is the filename: filename.py
What is the destination file: new_file.py
What is the host: [Public or Private IP of Server]
What is the port: 7190
Done
```

If port forwarding is enabled for the computer running server.py, the public ip of the 
network can be used by the client.  
Enter the IPv4 of the server computer if client and server are on the same network.  
Enter the public IP
of the network on which server.py is running if they are not.  