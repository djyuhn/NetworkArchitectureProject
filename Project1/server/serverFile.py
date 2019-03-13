import socket
import os
import struct


def main():
    host = '10.10.1.1'
    port = 5000
    sock = socket.socket()
    sock.bind((host,port))
    sock.listen(1)
    c,addr = sock.accept()

    while True:
        data = receive_message(c)
        data_decoded = data.decode()
        if data_decoded == 'EXIT':
            response = "Server is shutting down. Goodbye"
            # c.sendall(response.encode())
            send_message(c, response.encode())
            break
        else:
            if not os.path.exists("../data"):
                os.makedirs("../data")

            with open("../data/hello_client_server.txt", "w+") as file:
                file.write(data_decoded)

            print(data_decoded)
            response = data_decoded + "\nThe server says Hello! It added this line.\n\n"

            send_message(c, response.encode())

    c.close()
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
