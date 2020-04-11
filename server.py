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
	upperMsg = msg.upper()
	print('The client at {} says {!r}'.format(clientAddress, message))
	reply = upperMsg.encode('ascii')
	s.sendto(reply,client)