import socket

# SERVER = input()
# PORT = int(input())
SERVER = "127.0.0.1"
PORT = 6665
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(0.5)

try:
	client.connect((SERVER, PORT))
	answer = client.recv(1024)
	print("Example : 4 + 5")
	print("Type 'Over' to terminate")
except:
	exit("Server busy")

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
