import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost' , 4545))

string=input("enter a string: ")

client_socket.send(string.encode())

msg=client_socket.recv(1024).decode()

print("server: ", msg)