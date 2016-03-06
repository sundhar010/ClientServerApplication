
############################################################################################################################################
#                                                       Client side of client server communication                                         #

MYPORT = 8080                                          # port for client sever commuication 
IP_REQUEST_PORT = 9000                                 # Port for requesting server for its ip                    
IP_RECEVE_PORT = 7000                                  # port for receving the servers ip as respoce


import os,sys
import socket
import thread


def dspMsg(s):                                        #
	while True:                                   #
		data = s.recv(1024)                   #  function used by a thread to display the msg sent from the client
		print ">>" + str(data)                #
		pass                                  #



def sendMsg(s):                                       #
	while True:                                   #
		message = raw_input("")               #
		if message == "quit()":               #  function used by a thred to send the msg to the server
			s.close()                     #
			os._exit(1)                   #
		s.send(message)                       #
		pass                                  #



def getserver( ):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         #
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)       #
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #
	s.sendto("who is the server?", ('<broadcast>', IP_REQUEST_PORT))#
	s.close()                                                   #
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         #
	s.bind(("",IP_RECEVE_PORT))                                 #this function broadcasts that it wants the ip of server , receves the 
	data = ""                                                   #ip when the server replyes and returns it .
	while not len(data):                                        #
		data, addr = s.recvfrom(1024)                       #
		pass                                                #
	print data                                                  #
	sip = addr[0]                                               #
	print sip                                                   #
	s.close()                                                   #
	return sip                                                  #



def main():
	
	port = MYPORT
	host = getserver()
	s = socket.socket()
	s.connect((host,MYPORT))
	thread.start_new_thread(dspMsg,(s,)) #thread used for desplaying the msgs
	thread.start_new_thread(sendMsg,(s,))#thread used for sending msgs
	while 1:
		pass



if __name__ == '__main__':
	main()
