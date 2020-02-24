#darshan lal
#1001667684
#Proxy server program
#One must use python 2.7 to execute the code


from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import time,os
import urlparse
from urllib2 import urlopen

#Asking the user to enter the port
PORT=input("Port? =")

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
	#print self.path
	message= "GET request,\nPath: " + str(self.path) + "\nHeaders: " + str(self.headers)
	print "\nHTTP Get request from client \n",message
	
	#parsing the url to get the file name
	#ref: https://stackoverflow.com/questions/18727347/how-to-extract-a-filename-from-a-url-append-a-word-to-it
	link=str(self.path)
	a = urlparse.urlparse(link)
        filename=os.path.basename(a.path)
        print("Filename = ",filename)
	#filename="cachefile.txt"

	#fetching the file in cache
	#ref:https://www.mediafire.com/folder/5c1s...
	if os.path.isfile(filename):
		message="Cache Hit"
                print(message)
		
		#send the response stored in the cache
		if os.path.isfile(filename):
			with open(filename, 'rb') as f:
                                message = f.read()
				
				#Sending the response to the client
	                	self.wfile.write(message)
        	        	self.wfile.write('\n')
				print "Response successfully sent !"
	
	else:
		#if requested file do not exist on the the proxy server
		message="Cache Miss"
		print(message)
		
		#getting response from server 
		#Downloading the file from the internet
                #ref: https://stackoverflow.com/questions/43048132/download-text-file-from-url-python
                try:
			response = urlopen(link)
			response_headers=response.info()
			print response_headers
                	data = response.read().decode('ascii')
                	#txt_str = str(data)
                	print "Download Complete!"
                	#lines = txt_str.split("\\n")
                	#des_url = 'folder/forcast.csv'
                	fx = open(filename,"wb")
                	#for line in lines:
                	#fx.write(line+ "\n")
                
			fx.write(data)
			fx.close()
		except:
			fx = open(filename,"wb")
			data="Http Error : 404 file not found"
			fx.write(data)
       		
		if os.path.isfile(filename):
                        with open(filename, 'rb') as f:
                                message = str(f.read())
				
				#Sending the response to the client
                                self.wfile.write(message)
                                self.wfile.write('\n')

                                print "Response successfully sent !" 
        return


#Threadmixin is a library for assiging each client with a single thread to handle the client
#https://docs.python.org/2/library/socketserver.html
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', PORT), Handler)
    print'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()

