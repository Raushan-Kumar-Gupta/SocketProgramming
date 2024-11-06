import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 4545))
server_socket.listen(2)
print("listening...")
conn, client_add=server_socket.accept()
print("connected...")
data=conn.recv(1024).decode()

num1, num2 = map(int, data.split()) 
res=num1+num2
conn.send(str(res).encode())