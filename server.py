# Import socket module
import socket

# Here we use localhost ip address
# and port number
LOCALHOST = "127.0.0.1"
PORT = 8080
# calling server socket method
server = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8090))
server.listen(1)
print("Server started")
print("Waiting for client request..")
# Here server socket is ready for
# get input from the user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
# Running infinite loop
while True:
	data = clientConnection.recv(1024)
	msg = data.decode()
	if msg == 'Over':
		print("Connection is Over")
		break
	print("Equation is recievied")
	result = 0
	operation_list = msg.split()
	oprnd1 = operation_list[0]
	operation = operation_list[1]
	oprnd2 = operation_list[2]

	# here we change str to int converstion
	num1 = int(oprnd1)
	num2 = int(oprnd2)
	# Here we are perform basic arithmetic operation
	if operation == "+":
		result = num1 + num2
	elif operation == "-":

		result = num1 - num2
	elif operation == "/":
		result = num1 / num2
	elif operation == "*":
		result = num1 * num2

	print("Send the result to client")
	# Here we change int to string and
	# after encode send the output to client
	output = str(result)
	clientConnection.send(output.encode())
clientConnection.close()
