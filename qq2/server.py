import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost' , 4545))

print("server waiting for msg: ")

while True:
    data, client_address=server_socket.recvfrom(1024)
    data=data.decode()
    data=data.upper()
    server_socket.sendto(data.encode(), client_address)
