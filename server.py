import socket


host = socket.gethostbyname(socket.gethostname())
port = 9090 #chose any port number
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

#we will start to send/recive

server.listen(5)


while True:
    communication_socket, addr = server.accept()
    print(f"connected to {addr}")
    msg = communication_socket.recv(2**10).decode('utf-8')
    print(f"message from client is : {msg}")
    communication_socket.send(f"got your message! thx".encode('utf-8'))
    communication_socket.close()
    print(f"connection with {addr} over ")
