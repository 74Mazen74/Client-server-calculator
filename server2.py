import socket
from math import * 
import os
import argparse
import calendar as c
import time as t

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

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # If the port is busy then reuse it again
server.bind((SERVER, PORT))
server.listen(1)

log_file = open(f'{c.timegm(t.gmtime())}.log','a+',buffering=1)
clientNum = 0
print("Server started")
log_file.write(f'[{c.timegm(t.gmtime())}] Server started\n')
print("Waiting for any client request...")
log_file.write(f'[{c.timegm(t.gmtime())}] Waiting for any client request...\n')
while True:
    clientConnection, clientAddress = server.accept()
    clientConnection.sendall('Connected'.encode())
    print("New Client Connected")
    log_file.write(f'[{c.timegm(t.gmtime())}] New Client Connected\n')
    clientNum += 1
    pid = os.fork()
    if pid == 0:
        print(f'New child created to serve client number {clientNum}')
        log_file.write(f'[{c.timegm(t.gmtime())}] New child created to serve client number {clientNum}\n')

        while True: 
            data = clientConnection.recv(1024)
            msg = data.decode()
            if msg == '' or msg == 'Over':
                print(f'Client number {clientNum} connection is Over')
                log_file.write(f'[{c.timegm(t.gmtime())}] Client number {clientNum} connection is Over\n')
                break
            print(f'\tEquation = {msg} is recievied from client number {clientNum}')
            log_file.write(f'\t[{c.timegm(t.gmtime())}] Equation = {msg} is recievied from client number {clientNum}\n')
            try:
                result = eval(msg)
                print("\tEquation is solved")
                log_file.write(f'\t[{c.timegm(t.gmtime())}] Equation is solved\n')
                output = "Answer = "+str(result)
                print(f'\tSending result = {result} to client')
                log_file.write(f'\t[{c.timegm(t.gmtime())}] Sending result = {result} to client\n')
            except:
                print("\tWrong equation")
                log_file.write(f'\t[{c.timegm(t.gmtime())}] Wrong equation\n')
                output = "Wrong input, Please double check your equation"
            
            clientConnection.sendall(output.encode())
            print(f'\tResponse sent successfully to client number {clientNum}')
            log_file.write(f'\t[{c.timegm(t.gmtime())}] Response sent successfully to client number {clientNum}\n')
            print("--------------------------------------------")
        clientConnection.close()
log_file.close()
