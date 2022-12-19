import socket

# SERVER = input()
# PORT = int(input())
SERVER = "127.0.0.1"
PORT = 6666
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(0.5)

try:
	client.connect((SERVER, PORT))
	answer = client.recv(1024)
except:
	exit("Server busy")

while True:
	print("Example : 4 + 5")
	inp = input("Enter the operation in the form opreand operator oprenad: ")
	if inp == "Over":
		client.sendall(inp.encode())
		break
	# try:
	client.sendall(inp.encode())
	# except:
		# exit("Error")
	# try:
	answer = client.recv(1024)
	# except:
		# exit("Server busy")
	print("Answer is "+answer.decode())
	print("Type 'Over' to terminate")

client.close()
