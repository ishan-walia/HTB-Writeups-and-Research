# Socket
Socket programming is a way for two or more systems to communicate over a network.
A socket acts as an endpoint for communication between:
- Client ↔ Server
- Computer ↔ Computer
- Application ↔ Application

Python provides the built-in socket module for implementing network communication using protocols such as TCP and UDP.

# Features
- TCP Client-Server communication
- UDP communication
- Sending and receiving messages
- Multiple client connections
- IP address and port handling
- Basic network programming concepts
- Client-server architecture examples
- Error handling
- Socket configuration
- Network connection testing

# 🔌 TCP Socket Programming

TCP (Transmission Control Protocol) provides reliable, connection-oriented communication.

# TCP Server
```py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Waiting for connection...")

client, address = server.accept()

print(f"Connected: {address}")

while True:
    data = client.recv(1024)

    if not data:
        break

    print("Client:", data.decode())

    client.sendall(b"Message received")

client.close()
server.close()
```

# TCP Client
```
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

client.sendall(b"Hello Server")

response = client.recv(1024)

print("Server:", response.decode())

client.close()
```
- Run
- Open two terminals.
- Terminal 1:
- python server.py
- Terminal 2:
- python client.py

# 📡 UDP Socket Programming

UDP (User Datagram Protocol) is connectionless and generally faster than TCP, but it does not guarantee delivery.

# UDP Server
```py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 5000))

print("UDP server started...")

while True:
    data, address = server.recvfrom(1024)

    print(f"Client {address}: {data.decode()}")

    server.sendto(b"Message received", address)
```
UDP Client
```py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(
    b"Hello UDP Server",
    ("127.0.0.1", 5000)
)

data, address = client.recvfrom(1024)

print("Server:", data.decode())

client.close()
```
