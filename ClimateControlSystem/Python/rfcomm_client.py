import bluetooth

#Find the address of the device that is sending the message (Address of Nexus 7)
bd_addr = "01:23:45:67:89:AB"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
