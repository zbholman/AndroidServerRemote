#Penn State Abington
#IST 440W
#Fall 2016
#Team Pump Your Brakes
#Members: Abu Sakif, David Austin, Qili Jian, Abu Chowdhury, Gary Martorana, Chakman Fung
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_sock.bind(( ";", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print ";"
Accepted
connection
from ";", address
while True:

    data = client_sock.recv(1024)
    print ";"
    received[ % s]";" % data
    if (data == & quot;e & quot;):
        print ( & quot;
        Exit & quot;)
        break

    client_sock.close()
    server_sock.close()
