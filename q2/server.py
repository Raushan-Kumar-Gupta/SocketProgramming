import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 4567))

server.listen(2)

conn, address= server.accept()

with open('filetosend.txt', 'rb') as file:

    data=file.read()

conn.send(data)