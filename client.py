import socket
import sys
# SERVER = input()
# PORT = int(input())
SERVER = str(sys.argv[1])
PORT = int(sys.argv[2])
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(0.5)

try:
	client.connect((SERVER, PORT))
	answer = client.recv(1024)
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

	print("Answer is "+answer.decode())
	

client.close()
