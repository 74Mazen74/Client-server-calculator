import socket

LOCALHOST = "127.0.0.1"
PORT = 5050
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
while True:
	clientConnection, clientAddress = server.accept()
	print("Connected client :", clientAddress)
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
			clientConnection.send(output.encode())
		except:
			break
	clientConnection.close()
