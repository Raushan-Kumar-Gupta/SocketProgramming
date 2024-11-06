import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(('127.0.0.1', 4567))

msg=server.recv(1024)

with open('received.txt', 'wb') as file:
    file.write(msg)