import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost' , 4545))
server_socket.listen(2)
print('server is listening....')

conn, address=server_socket.accept()
print("server is connected...")

string=conn.recv(1024).decode()
string=string.upper()

conn.send(string.encode())