import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 4545))

data=client_socket.recv(1024).decode()

with open('cba.txt', 'w') as file:
    file.write(data)