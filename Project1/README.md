# Network Architecture I - Project 1

This project for Network Architecture I is split into two parts.

## Part 1:

### Task:
Develop and deploy a simple TCP client and server programs on [GENI](https://portal.geni.net/). To demonstrate the functionality of the programs, screenshots of the exchanges will be provided.

The tasks for this part are split into the following subparts, Part A and Part B:

#### Part A

 * Have the client message, “Hello from Client: DJ Yuhn” to the server.
 * Have the server respond with, "Hello from Server: DJ Yuhn".
 * Have the messages echo between the client and server nodes.
 * Quit the program by typing, "Bye from Client: DJ Yuhn".
 * Have server respond, "Bye from Server: DJ Yuhn".

#### Part B

- Have the client message send a large text file greater than 10KB to the server.
- Have the server print the contents of this file to the screen.
- Have the server save the file locally.
- Have the server append a new line to the file (ex: "Hello from the Server!") before returning the updated file to the client.
- Have the client print the contents of this file to the screen.

### Steps

In this section I will provide an overview of the process in creating the resources for the first part of the project. Part A of this section will provide screenshots and gifs of the process to create the resources and sending a message from the client node to the server node and then the server responding.

Part B of this section will provide a gif and a screenshot of the process to transfer a file of size greater than 10 KB from the client node to the server node. The size of this file is roughly 18KB, as seen under the `data` directory of this project. The server then saves this file locally and returns back the file to the client with an appended message of the server saying Hello!



#### PART A

To begin, a slice was created on the GENI Portal with two resources: client and server.

![Slice_Resources](docs/screenshots/Slice_Resources.png)

With the resources created, each node was connected to using Putty and a private SSH key. The language used for this project was Python and the PyCharm IDE was used.

To send the files to the nodes, PSFTP was used to securely send the files through an SSH connection. The server node received the files relevant for the server, and the client node received the files relevant for the client and the `hello_client_server.txt`

![PSFTP-Code-Server](docs/screenshots/PSFTP-Code-Server.png)
Screenshot of PSFTP commands and directories for Server node.

![PSFTP-Code-Client](docs/screenshots/PSFTP-Code-Client.png)
Screenshot of PSFTP commands and directories for Client node.

With the respective code on each of the nodes, to demonstrate that the messages are being sent correctly from client to server and then a response from server to client, see the gif and image below.

![Client-Server-Demo](docs/screenshots/Client-Server-Demo.gif)

Gif of the client and server communicating a greeting.

Below is the final image:

![Client-Server-Hello](docs/screenshots/Client-Server-Hello.png)



#### PART B

In this section the client must transfer a file of size greater than 10 KB to the server. The server will save this file locally and then append a message before returning the file to the client. Due to the file size, this part required specifying the length of the message to be sent in order to keep the socket open for continually retrieving the message. That is, if the message length was not sent and the message was greater than the buffer size specified then only a part of the message would be considered. Additionally, the TCP protocol may send the stream of bytes with various lengths, thus in the following code the length of the chunk needed to be considered rather than the entirety of the byte size expected when increasing the `running_byte_size` variable:

```python
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
```



![Client-Server-File-Transfer](docs/screenshots/Client-Server-File-Transfer.gif)

Gif of the client and server transferring a file.

![Client-Server-File-Transfer-End](docs/screenshots/Client-Server-File-Transfer-End.png)

Image of the final output of transferring a file.



## References

[Lipsum](https://www.lipsum.com/feed/html) - Used to generate text to meet the file size requirements

[SSH.com](https://www.ssh.com/ssh/putty/putty-manuals/0.68/Chapter6.html#psftp-starting) - Used for reference on transferring files using PSFTP