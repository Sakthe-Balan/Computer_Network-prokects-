import socket
import os
import pickle

# Initialize s to socket
s = socket.socket()

# Initialize the host
host = "192.168.151.158"

# Initialize the port
port = 8080

# connect to the server
s.connect((host, port))

print("Connected to server")

# take command as input
command = input(str("Enter Command :"))
s.send(command.encode())

# send file to server
if command == "send":
    filename = input("Enter filename with extension: ")
    size = os.path.getsize('./'+filename)

    with open(filename, "rb") as f:
        file_data = f.read()

    obje = {
        "filename": filename,
        "size": size,
        "code": file_data
    }

    obje = pickle.dumps(obje)
    s.send(obje)
# receive the confirmation
data = s.recv(1024)

if data:
    print(data.decode())