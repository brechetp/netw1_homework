import socket

def geturl ( url ):
 request = b"GET / HTTP/1.1\nHost: "+url+"\n\n"
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 s.connect((url , 80))
 s.sendall(request)
 print s.recv(10000)
 s.close

geturl ("stackoverflow.com")
