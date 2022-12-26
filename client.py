import socket
import argparse

parser = argparse.ArgumentParser(description='Multiple Clients Server app')
parser.add_argument('-d','--address', help='Address to start server on', required=True)
parser.add_argument('-p','--port', help='Port to start listening on', required=True)

# SERVER = "127.0.0.1"
# PORT = 6060

# SERVER = input()
# PORT = int(input())

args = vars(parser.parse_args())
SERVER = str(args['address'])
PORT = int(args['port'])

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(0.5)
try:
	client.connect((SERVER, PORT))
	answer = client.recv(1024)
	print(answer.decode())
	print("Example : 4 + 5")
	print("Type 'Over' to terminate")
except:
	exit("Server busy")
client.settimeout(10000)

while True:
	try:
		inp = input("Enter the operation in the form opreand operator oprenad: ")
	except:
		exit("Client closed")
	if inp == "Over":
		client.sendall(inp.encode())
		break
	client.sendall(inp.encode())

	answer = client.recv(1024)

	print(answer.decode())
	

client.close()
