import socket

c = socket.socket()
c.connect(('127.0.1.1', 23456))
name = input("enter your name : ")
c.send(name.encode())
print("Message from server : ", c.recv(1024).decode())
