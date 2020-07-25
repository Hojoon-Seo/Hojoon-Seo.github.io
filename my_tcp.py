import socket

HOST = "www.google.com"
PORT = 80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
response = s.recv(4096)
print(response)
