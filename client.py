import socket

MAX_SIZE_BYTES = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("enter a msg to server ")

data = msg.encode('ascii')

s.sendto(data,("127.0.0.1",3000))

data,server = s.recvfrom(MAX_SIZE_BYTES)

recv_msg = data.decode('ascii')

print('The server at {} says {!r}'.format(server,recv_msg))