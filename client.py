import socket

MAX_SIZE_BYTES = 65535

server_name = "127.0.0.1"
server_port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((server_name,server_port))
msg = input("enter a msg to server ")

data = msg.encode('ascii')

s.send(data,(server_name,server_port))

data,server = s.recvfrom(MAX_SIZE_BYTES)

recv_msg = data.decode('ascii')

print('The server at {} says {!r}'.format(server,recv_msg))