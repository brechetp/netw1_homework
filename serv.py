import socket

PORT=4444
HOST="127.0.0.1"

srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.bind((HOST,PORT))
srv.listen(1)

f = open('database','w')

conn,addr=srv.accept()
print "Connected by %s:%d"%addr
while True:
 data=conn.recv(1024)
 if not data: break
 f.write(data)
 f.write("\n")

f.close()
conn.close()
