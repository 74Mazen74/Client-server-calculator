import socket
from math import * 
import argparse

parser = argparse.ArgumentParser(description='Single Client Server app')
parser.add_argument('-d','--address', help='Address to start server on', required=True)
parser.add_argument('-p','--port', help='Port to start listening on', required=True)

# SERVER = "127.0.0.1"
# PORT = 6060

# SERVER = input()
# PORT = int(input())

args = vars(parser.parse_args())
SERVER = str(args['address'])
PORT = int(args['port'])

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # If the port is busy then reuse it again
server.bind((SERVER, PORT))
server.listen(1)
print("Server started")
while True:
	print("Waiting for new client request...")
	clientConnection, clientAddress = server.accept()
	clientConnection.sendall('Connected'.encode())
	print("New Client Connected")
	while True: 
		data = clientConnection.recv(1024)
		msg = data.decode()
		if msg == '' or msg == 'Over':
			print("Connection is Over")
			break
		print(f'\tEquation = {msg} is recievied')
		try:
			result = eval(msg)
			print("\tEquation is solved")
			output = "Answer = "+str(result)
			print(f'\tSending result = {result} to client')
		except:
			print("\tWrong equation")
			output = "Wrong input, Please double check your equation"
		
		clientConnection.sendall(output.encode())
		print("\tResponse sent successfully")
		print("--------------------------------------------")
	clientConnection.close()
	server.settimeout(100000) # Make large tiemout to wait for new client
