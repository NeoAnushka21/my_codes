import socket

# This is the socket on client side
c = socket.socket()

# Connecting to (server host,port)
c.connect(('127.0.1.1', 23456))

# Take name as input from Client side
name = input("enter your name : ")

# Sending name in encoded form
c.send(name.encode())

# Receiving message from server and decoding it'
print("Message from server : ", c.recv(1024).decode())
