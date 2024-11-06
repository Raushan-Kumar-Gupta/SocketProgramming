import socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 4545))

num1=input("enter 1st number: ")
num2=input("enter 2nd number: ")

client_socket.send(f"{num1} {num2}".encode())
data=client_socket.recv(1024).decode()
print("sum= ", data)
