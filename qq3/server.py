import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 4545))
server_socket.listen(2)
print("server is listening...")

conn, client_addr=server_socket.accept()

print("server connected...")

with open('abc.txt', 'r') as file:
    data=file.read()
    print(data)
    conn.send(data.encode())