import socket
import os
import pickle
# Initialize s to socket
s = socket.socket()

# Initialize the host
host = ""

# Initialize the port
port = 8080

# Bind the socket with port and host
s.bind((host, port))

print("waiting for connections...")

# listening for connections
s.listen()

# accepting the incoming connections
conn, addr = s.accept()

print(addr, "is connected to server")

# receive the command from client program
command = conn.recv(1024)
command = command.decode()

# match the command and execute it on slave system
if command == "run_python":
    print("Command is :", command)
    conn.send("Command received".encode())

    # you can give batch file as input here
    os.system('python hello.py')

elif command == "send":
    print("Command is :", command)
    conn.send("Command received".encode())

    ans= conn.recv(2048)
    ans = pickle.loads(ans)
    filename = ans['filename']
    size = int(ans['size'])
    data = ans['code']
    # create a new file with the given filename and write the data to it
    with open(filename, "wb") as f:
       
        while len(data) < size:
            packet = conn.recv(size - len(data))
            if not packet:
                break
            data += packet
        f.write(data)

    # execute the file that was received
    os.system(f"python {filename}")
