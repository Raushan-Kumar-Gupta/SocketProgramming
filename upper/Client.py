import socket

# Create a TCP/IP socket

# Connect to the server
client_socket.connect(('localhost', 5678))

# Get user input and send it to the server
sentence = input("Enter a sentence: ")
client_socket.send(sentence.encode())

# Receive and display the response
response = client_socket.recv(1024).decode()
print("Uppercased Sentence from Server:", response)

client_socket.close()
