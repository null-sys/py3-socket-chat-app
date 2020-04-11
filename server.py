import socket

MAX_SIZE_BYTES  = 65535

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = 3000
hostname = "127.0.0.1"
s.bind((hostname,port))

print("server is on at ",s.getsockname())

while True:  #server is always listening
	data, client = s.recvfrom(MAX_SIZE_BYTES)
	msg = data.decode('ascii')
	print(msg)
	reply = input("						")
	reply = reply.encode('ascii')
	s.sendto(reply,client)