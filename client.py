import urllib2
files = urllib2.urlopen('http://wikipedia.org').read().splitlines()
#opfor l in files[:]: print l.split()[-1]
print files
