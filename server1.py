import socket

LOCALHOST = "127.0.0.1"
PORT = 6666
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")
while True:
	clientConnection, clientAddress = server.accept()
	clientConnection.sendall('Connected'.encode())
	while True: 
		try: 
			msg = ''
			data = clientConnection.recv(1024)
			msg = data.decode()
			if msg == '' or msg == 'Over':
				print("Connection is Over")
				break
			print("Equation is recievied")
			result = eval(msg)
			print("Send the result to client")
			output = str(result)
			clientConnection.sendall(output.encode())
		except:
			break
	clientConnection.close()
	server.settimeout(0.5)
	try:
		clientConnection, clientAddress = server.accept()
		clientConnection.sendall('Connected'.encode())
	except:
		exit("Server closed")
