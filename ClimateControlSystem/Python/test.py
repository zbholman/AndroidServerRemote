import bluetooth
import RPi.GPIO as GPIO
import time
import os
import glob
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Gets the ID of temperature sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Opens folder for temperature sensor
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Reads the temperature coming from sensor
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0 #Celsius temperature 
        temp_f = temp_c * 9.0 / 5.0 + 32.0 #Fahrenheit temp
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",1))
server_sock.listen(1)

port = server_sock.getsockname()[1]

print "Waiting for connection on RFCOMM channel %d" % port
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

while True:
        data=client_sock.recv(1024)
        #client_sock.send(str(int(read_temp())))
        #print ("sending %s" % read_temp())

        
        if data == "0":
               # GPIO.output(24,GPIO.HIGH)
                print("AC ON")
        elif data == "1":
               # GPIO.output(24,GPIO.LOW)
                print("AC OFF")
        
'''
loopStart = time.time()
timePassed = 0.0
timePassed1= 0.0
timePassed2= 0.0
#client_sock.send(str(read_temp()))
#print ("sending %s" % read_temp())
while timePassed < 100 :
        loopStart1= time.time()
        while timePassed1 <4:
client_sock.send(str(read_temp()))                      
                print ("sending %s" % read_temp())
                now=time.time()
                timePassed1 = now - loopStart1
        
        loopStart2= time.time()
        while timePassed2 <4:
                now1= time.time()
                timePassed2 = now1 - loopStart2
                if client_sock.recv(1024) == "0":
                        print ("LED OFF")
                        GPIO.output(23,GPIO.HIGH)
                elif client_sock.recv(1024) == "1":
                        print ("LED ON")
                        GPIO.output(23,GPIO.LOW)
        timePassed= 0.0
        timePassed1=0.0
        timePassed2=0.0 
        #client_sock.send(str(read_temp()))
        #print ("sending %s " % data)
'''
client_sock.close()
server_sock.close() 

