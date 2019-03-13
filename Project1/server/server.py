import socket
host = '10.10.1.1'
port = 5000
socket = socket.socket()
socket.bind((host,port))
socket.listen(1)
c,addr = socket.accept()

while True:
        data = c.recv(1024)
        if data == 'Bye from Client: DJ Yuhn':
                c.send('Bye from Server: DJ Yuhn')
                break
        elif data == 'Hello from Client: DJ Yuhn':
                print(str(data))
                c.send('Hello from Server: DJ Yuhn')
        else:
                response = "You sent me the following message:\n" + data
                print(str(data))
                c.send(response)
c.close()
