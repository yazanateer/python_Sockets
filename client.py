import socket

host ='10.0.0.12' #you can change it
port = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

socket.send("hello client".encode('utf-8'))
print(socket.recv(1024))