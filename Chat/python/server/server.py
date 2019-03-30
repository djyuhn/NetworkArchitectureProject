import socket
import struct
from threading import Thread

HOST = '10.10.1.1'
PORT = 5000
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.bind((HOST, PORT))
CLIENTS = {}


def main():
    SOCK.listen(6)
    print('Python Server has begun.\nWaiting for connections...')
    try:
        while True:
            accept_thread = Thread(target=accept_incoming_clients())
            accept_thread.start()
            accept_thread.join()
    finally:
        SOCK.close()


def accept_incoming_clients():
    while True:
        client, address = SOCK.accept()
        print("[%s] has connected..." % ('{}:{}'.format(address[0], address[1])))
        greeting = "Server welcomes you to the chat.\nEnter your name: "
        send_message(client, greeting)
        Thread(target=handle_client, args=(client, address)).start()


def handle_client(client, address):
    name = receive_message(client)
    greeting = "Server welcomes %s. To quit, type #quit" % name
    send_message(client, greeting)
    announcement = "%s from [%s] has connected with the server." % (name, '{}:{}'.format(address[0], address[1]))
    announce_all(announcement)
    CLIENTS[client] = name
    while True:
        receive = receive_message(client)
        if str.lower(receive) != "#quit":
            announce_all(receive, name + ': ')
        else:
            send_message(client, "#quit")
            client.close()
            del CLIENTS[client]
            announce_all("%s has left." % name)
            break


def announce_all(message, prefix=''):
    for sock in CLIENTS:
        send_message(sock, prefix + message)


def send_message(sock, message):
    message = struct.pack('!I', len(message)) + message.encode()
    sock.sendall(message)


def receive_message(sock):
    raw_message_length = _receive_all(sock, 4)
    if not raw_message_length:
        return None
    message_length = struct.unpack('!I', bytes(raw_message_length, 'utf-8'))[0]
    return _receive_all(sock, int(message_length))


def _receive_all(sock, byte_size):
    running_byte_size = 0
    data_fragments = []
    while running_byte_size < byte_size:
        byte_difference = byte_size - running_byte_size
        chunk = sock.recv(byte_difference)
        if not chunk:
            return None
        data_fragments.append(chunk)
        running_byte_size += len(chunk)

    return b"".join(data_fragments).decode("utf-8")


if __name__ == "__main__":
    main()
