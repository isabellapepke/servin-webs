#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

#This class will handle any incoming request from the brower
class myHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		#Send the html message
		self.wfile.write("Hello world!")
		return


try:
	#create a webserver and define the handeler to maage the incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port', PORT_NUMBER)

	#Wait forever for incoming htto request
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
