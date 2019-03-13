import socket
import struct


def main():
    host = '10.10.1.1'
    port = 5000
    sock = socket.socket()
    sock.connect((host,port))
    message = input("To exit, type EXIT" + "\n" + "To send file, press ENTER: ")

    file = open('../data/hello_client_server.txt', 'rb')
    file_contents = file.read()

    while True:
        if message == "EXIT":
            # sock.sendall(message.encode())
            # data = receive_all(sock)
            send_message(sock, message.encode())
            data = receive_message(sock).decode()
            print(data)
            break
        else:
            # sock.sendall(file_contents)
            # data = receive_all(sock).decode()
            send_message(sock, file_contents)
            data = receive_message(sock).decode()
            print(data)
            message = input()

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
