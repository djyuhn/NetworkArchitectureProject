import socket

host = '10.10.1.1'
port = 5000
socket = socket.socket()
socket.connect((host,port))
message = input("Enter:: ")

while True:
    if message == 'Bye from Client: DJ Yuhn':
            socket.send(message.encode())
            data = socket.recv(1024)
            print(data.decode())
            break
    elif message == 'Hello from Client: DJ Yuhn':
            socket.send(message.encode())
            data = socket.recv(1024)
            print(data.decode())
            message = input()
    else:
            socket.send(message.encode())
            data = socket.recv(1024)
            print(data.decode())
            message = input()

socket.close()
