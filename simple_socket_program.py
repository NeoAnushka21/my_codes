import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created successfully")
except socket.error:
    print("oops! cannot create")

port = 80
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("host error")
    sys.exit()

s.connect((host_ip, port))
print("socket creation successful")
