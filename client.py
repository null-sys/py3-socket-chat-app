import socket

MAX_SIZE_BYTES = 65535

server_name = "127.0.0.1"
server_port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((server_name,server_port))

recv_msg = ""
while recv_msg != "bye":
	msg = input("          				")
	data = msg.encode('ascii')
	s.send(data)
	data,server = s.recvfrom(MAX_SIZE_BYTES)
	recv_msg = data.decode('ascii')
	print(recv_msg)