import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5678))
server_socket.listen(1)

print("Server is waiting for a connection...")

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if data:
        # Convert data to uppercase
        response = data.upper()
        # Send response back to the client
        client_socket.send(response.encode())
    
    client_socket.close()
