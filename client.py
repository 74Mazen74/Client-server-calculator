import socket


SERVER = input()
PORT = int(input())
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
	
while True:
	print("Example : 4 + 5")
	inp = input("Enter the operation in the form opreand operator oprenad: ")
	if inp == "Over":
		client.send(inp.encode())
		break
	try:
		client.sendall(inp.encode())
	except:
		exit("Error")
	answer = client.recv(1024)
	print("Answer is "+answer.decode())
	print("Type 'Over' to terminate")

client.close()
