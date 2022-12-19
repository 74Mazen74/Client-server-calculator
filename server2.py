import socket
import os
LOCALHOST = "127.0.0.1"
PORT = 6669
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")

while True:
    clientConnection, clientAddress = server.accept()
    clientConnection.sendall('Connected'.encode())
    pid = os.fork()
    print("New child created")
    if pid == 0:
        print("New child serving")
        while True: 
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
        clientConnection.close()
	# server.settimeout(100000)
