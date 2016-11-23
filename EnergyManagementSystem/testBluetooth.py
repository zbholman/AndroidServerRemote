import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )

port = 1
server_sock.bind(("",1))
server_sock.listen(1)

port = server_sock.getsockname()[1]

print ("Waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print ("Accepted connection from ", client_info)

client_sock.close()
server_sock.close()
