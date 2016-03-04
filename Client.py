import socket
import thread
def dsp(s):
	while True:
		data = s.recv(1024)
		print "msg >" + str(data)
		pass
def msg(s):
	while True:
		message = raw_input(">>")
		s.send(message)
		if message == 'q':
			s.close()
			break
		pass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('127.0.0.1',12345))
print "my ip addres " + str(s.getsockname()[0])
host = '127.0.0.1'
port = 3300
s = socket.socket()
s.connect((host,port))
thread.start_new_thread(dsp,(s,))
thread.start_new_thread(msg,(s,))
while 1:
	pass
