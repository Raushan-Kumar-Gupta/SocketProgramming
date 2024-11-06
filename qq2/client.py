import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

string=input("enter a string: ")
client_socket.sendto(string.encode(), ('localhost', 4545))
data, server_addr=client_socket.recvfrom(1024)
data=data.decode()
print("server: ", data)
client_socket.close()
