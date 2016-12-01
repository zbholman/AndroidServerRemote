import bluetooth
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",1))
server_sock.listen(1)

port = server_sock.getsockname()[1]

print "Waiting for connection on RFCOMM channel %d" % port
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

while True:
        data=client_sock.recv(1024)        
        if data == "acON":
               GPIO.output(23,GPIO.LOW)
               print("AC ON")
        elif data == "acOFF":
               GPIO.output(23,GPIO.HIGH)
               print("AC OFF")
        elif data == "heatON":
               GPIO.output(24,GPIO.LOW)
               print("HEAT ON")
        elif data == "heatOFF":
               GPIO.output(24,GPIO.HIGH)
               print("HEAT OFF")
        
client_sock.close()
server_sock.close() 

