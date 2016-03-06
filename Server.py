############################################################################################################################################
#                                                       Server side of client server communication                                         #


IP_REQUEST_PORT = 9000                                           # port used for accepting client's request for server's ip
IP_SEND_PORT = 7000	                                         # port used for sending servers ip
MYPORT = 8080                                                    # port for server client communication
NoClients =  3                                                   # number of clients which server accept
lis=[]                                                           # List of all client's sockets which are connected to server

import sys,os
import socket 
import thread


def sendip():
	while True:
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)        #  
		s.bind(("",IP_REQUEST_PORT))                               #  
		data = ""                                                  #
		while not len(data):                                       #  Server Waiting For the request from the client for it's IP
			data, addr = s.recvfrom(1024)                      #
		print data                                                 #
		s.close()                                                  #


		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)        #
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)	   #
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)    #  server replying the client with its ip
		s.sendto("I am the Server", ('<broadcast>', IP_SEND_PORT)) #
		s.close()                                                  #
		pass                                                       #


def dspMsg(c):                                                             #
	while True:                                                        #
		data = c.recv(1024)                                        #
		if not data:                                               #  function used by a thread to display client's msgs
			break                                              #  
		print " >>"+ str(data)                                     #
		pass                                                       #
	c.close()                                                          #




def sendMsg():                                                             #
	while True:                                                        #
		data = raw_input("")                                       #
		if data == "quit()":                                       #
			for c in lis:                                      #
				c.close()                                  #
			os._exit(1)                                        #
		for c in lis:	                                           #  function used by a thread to send server's msg to all the clients 
			c.send(data)                                       #    connected to the server
			pass                                               #
		pass                                                       #



def Main():
	thread.start_new_thread(sendip,()) #Thread which runs sendip function
	host = "localhost"
	port = MYPORT
	s = socket.socket()
	s.bind(('',port))
	thread.start_new_thread(sendMsg,()) #Thread which runs sendMsg function
	while 1:
		s.listen(3)
		c , addr = s.accept()
		lis.append(c)
		print "connected to :"+ str(addr)
		thread.start_new_thread(dspMsg,(c,)) #Thread which runs dspMsg function
		pass	
	

if __name__ == '__main__':   
	Main()
