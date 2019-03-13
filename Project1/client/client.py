import socket
host = '10.10.1.1'
port = 5000
socket = socket.socket()
socket.connect((host,port))
message = input("Enter:: ")

while True:
        if message == 'Bye from Client':
                socket.send(m)
                data=socket.recv(1024)
                print(str(data))
                break
        elif message == 'Hello from Client':
                socket.send(m)
                data=socket.recv(1024)
                print(str(data))
                m=input()
        else:
                socket.send(m)
                data = socket.recv(1024)
                print(str(data))
                m=input()

s.close()
