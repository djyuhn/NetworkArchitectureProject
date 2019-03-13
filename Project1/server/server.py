import socket

host = '10.10.1.1'
port = 5000
socket = socket.socket()
socket.bind((host,port))
socket.listen(1)
c,addr = socket.accept()
response = ""

while True:
    data = c.recv(1024)
    data_decoded = data.decode()
    if data_decoded == 'Bye from Client: DJ Yuhn':
        response = "Bye from Server: DJ Yuhn"
        c.send(response.encode())
        break
    elif data_decoded == 'Hello from Client: DJ Yuhn':
        print(str(data_decoded))
        response = "Hello from Server: DJ Yuhn"
        c.send(response.encode())
    else:
        response = "You sent me the following message:\n" + data_decoded
        print(str(data_decoded))
        c.send(response.encode())
c.close()
