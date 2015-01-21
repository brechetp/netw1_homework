import socket
import re

def geturl ( url ):
 request = b"GET / HTTP/1.1\nHost: "+url+"\n\n"
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 s.connect((url , 80))
 s.sendall(request)
 result = s.recv(4096)
 accu = result
 while (len(result)>0):
  print 'ok'
  result = s.recv(4096)
  accu += result
 return accu
 s.close

def filter(string):
 pattern = ".*(<table .*\n <caption>\n .* List of studio album .*\n </table>).*"
 prog = re.compile(string)
 result = prog.match(string)
 return result


