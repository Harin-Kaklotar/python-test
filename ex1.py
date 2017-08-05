from sys import argv

script, fileName = argv

print "your script name: %r " % script
print "your file name is: %r " %fileName

print "now we are opning file"

filen = open(fileName)

readFile = filen.read()

print "And the file says: %r" %readFile
