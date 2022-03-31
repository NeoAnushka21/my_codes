import socket

# this is the socket on client side
c = socket.socket()

# connecting to (server host,port)
c.connect(('127.0.1.1', 23456))

# Take name as input from Client side
name = input("enter your name : ")

# Sending name in encoded form
c.send(name.encode())

# receiving message from server and decoding it'
print("Message from server : ", c.recv(1024).decode())
