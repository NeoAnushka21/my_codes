# importing socket library
import socket

# creating object for socket class
s = socket.socket()

# to get localhost on your machine
local_host_name = socket.gethostname()

# to fetch ip address of the local host
ip_addr = socket.gethostbyname(local_host_name)

print('host-name:', local_host_name, 'ip-address:', ip_addr)
print("socket created")

# binding the socket with server and port
s.bind((ip_addr, 23456))

# allows maximum of 1 connection to the socket
s.listen(1)
print('Waiting for connections:')

while True:

    # waiting will client accepts the connection
    # c- client socket, c_addr- client address
    c, c_addr = s.accept()

    # receiving name from client and decoding it
    name = c.recv(1024).decode()
    print("connected to ", c_addr, "Clients Name:", name)

    # sending message to the client in binary encoded string
    c.send('Welcome to my page!!'.encode())

    # to close loop when client will type exit as name
    if name == 'exit':
        break

    c.close()
