import socket
import os
import struct


def main():
    host = '10.10.1.1'
    port = 5000
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    client, addr = sock.accept()

    while True:
        data = receive_message(client)
        data_decoded = data.decode()
        if str.lower(data_decoded) == 'exit':
            response = "Server is shutting down. Goodbye"
            send_message(client, response.encode())
            break
        else:
            print(data_decoded)
            response = ""
            send_message(client, response.encode())

    client.close()
    sock.close()


def send_message(sock, message):
    message = struct.pack('!I', len(message)) + message
    sock.sendall(message)


def receive_message(sock):
    raw_message_length = receive_all(sock, 4)
    if not raw_message_length:
        return None
    message_length = struct.unpack('!I', bytes(raw_message_length))[0]
    return receive_all(sock, message_length)


def receive_all(sock, byte_size):
    running_byte_size = 0
    data_fragments = []
    while running_byte_size < byte_size:
        byte_difference = byte_size - running_byte_size
        chunk = sock.recv(byte_difference)
        if not chunk:
            return None
        data_fragments.append(chunk)
        running_byte_size += len(chunk)

    return b"".join(data_fragments)


if __name__ == "__main__":
    main()
