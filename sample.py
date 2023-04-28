import socket

# Choose an available UDP port number
UDP_PORT = 12345

# Create a UDP socket and bind it to the chosen port
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('localhost', UDP_PORT))

# Print a message indicating that the socket is listening
print(f"Listening for UDP packets on port {UDP_PORT}...")

# Receive and print any UDP packets that are sent to the socket
while True:
    data, address = udp_socket.recvfrom(1024)
    print(f"Received {len(data)} bytes from {address}")
    print(f"Data: {data}")
