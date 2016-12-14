import time,bluetooth


server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)

port = server_sock.getsockname()[1]

print "Waiting for connection on RFCOMM channel %d" % port 
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

#client_sock.recv(1024)
for i in range(100):
	time.sleep(0.5)
	print(i)
	client_sock.send(str(i))
