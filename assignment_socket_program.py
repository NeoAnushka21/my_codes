import socket

s = socket.socket()
local_host_name = socket.gethostname()
ip_addr = socket.gethostbyname(local_host_name)
print('host-name:', local_host_name, 'ip-address:', ip_addr)
print("socket created")

s.bind((ip_addr, 23456))
s.listen(1)
print('Waiting for connections:')

while True:
    c, c_addr = s.accept()
    name = c.recv(1024).decode()
    # name1 = c.recv(1024)
    print("connected to ", c_addr, "Clients Name:", name)
    print(type(name))
    # c.send(bytes("welcome!!", 'utf-8'))
    c.send('Welcome to my page!!'.encode())

    if name == 'exit':     # to close loop when client will say exit
        break

    c.close()
