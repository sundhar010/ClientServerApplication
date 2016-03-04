import socket 
import sys
import thread
def dsp(c):
	print "dsp"
	while True:
		data = c.recv(1024)
		if not data:
			break
		print "Him >>"+ str(data)
		pass
	c.close()
def msg(c):
	print "msg"
	while True:
		data = raw_input("YOU >>")
		if data == 'q':
			c.close()
			quit()
		c.send(data)
		pass
def Main():
	host = "127.0.0.1"
	port = 3300
	s = socket.socket()
	s.bind((host,port))
	s.listen(2)
	c , addr = s.accept()
	print "connected :"+ str(addr)
	thread.start_new_thread(dsp,(c,))
	thread.start_new_thread(msg,(c,))
	while 1:
		pass	
	
	
if __name__ == '__main__':
	Main()
