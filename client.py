import socket

PORT=4444
HOST="127.0.0.1"

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect((HOST,PORT))

while True:
 cmd = raw_input("Input:  ")
 if len(cmd)==0: break
 cli.send(cmd)

cli.close()
