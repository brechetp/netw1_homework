import socket
import HTMLParser

class MyHTMLParser(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag 
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
        '<body><h1>Parse me! </h1></body></html>')

def string_from_file(filename):
 res=""
 for line in open(filename, 'r'):
  res += line
 return res
