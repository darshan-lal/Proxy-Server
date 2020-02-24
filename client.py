#darshan lal
#1001667684
#client program
#one should use python 2.7 to run this code

import httplib

#Asking the user for port no
PORT=input("Port? =")

#Using httplib connecting with the proxy server
#This library automatically takes care of the socket 
#https://docs.python.org/2/library/httplib.html
conn = httplib.HTTPConnection("localhost",PORT)

#asking the user for the URL where as if d is pressed it takes the default one
link= raw_input("Enter the URL or Enter'd' for default (http://gaia.cs.umass.edu/wireshark-labs/alice.txt):\n")

if link == "d":
	conn.request("GET","http://gaia.cs.umass.edu/wireshark-labs/alice.txt")
else:
	conn.request("GET", link)

r = conn.getresponse()

#Displaying the response from the server
print "\nResponse after decoding :\n ",r.read()
print "\nResponse In http formate :\n ",r
#print r.info()
print r.status, r.reason

#closing the connection
conn.close
