<<<<<<< HEAD
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
=======
import urllib2
files = urllib2.urlopen('http://wikipedia.org').read().splitlines()
#opfor l in files[:]: print l.split()[-1]
print files
>>>>>>> abcf159129d4140547354f2358dd37ac77bcad6a
