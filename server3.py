import socket
from math import *
import argparse
import json

from http_parser.parser import HttpParser
parser = argparse.ArgumentParser(description='Single Client Server app')
parser.add_argument('-d', '--address',
                    help='Address to start server on', required=True)
parser.add_argument(
    '-p', '--port', help='Port to start listening on', required=True)

# SERVER = "127.0.0.1"
# PORT = 6060

args = vars(parser.parse_args())
SERVER = str(args['address'])
PORT = int(args['port'])

p = HttpParser()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER, PORT))
server.listen(1)
print("Server started")
while True:
    print("Waiting for new HTTP request...")
    clientConnection, clientAddress = server.accept()
    print("New Request received")
    data = clientConnection.recv(10240)
    msg = data.decode()
    recved = len(data)
    res = ''
    try:
        nparsed = p.execute(data, recved)
        data = json.loads(p.recv_body().decode())

        for i in data['query']:
            res=eval(i['requestedLine'])
            i['result']=str(res)
        json_object = json.dumps(data, indent=4)
        res = b"""HTTP/1.1 200 OK\r\n
"""+json_object.encode()
        # print(res.decode())
        if res.decode() == '':
            raise Exception 
        clientConnection.sendall(res)
        print("Response sent successfully")
    except:
        print("Error in the request")
        res =  b"""HTTP/1.1 200 OK\r\n
Error\r\n"""
        clientConnection.sendall(res)
    clientConnection.close()
    server.settimeout(100000)  # Make large tiemout to wait for new client
