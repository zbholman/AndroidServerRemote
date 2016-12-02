import bluetooth
import RPi.GPIO as GPIO
import time
import os #Enable wire drivers and interface with sensor
import glob #Load drivers
import time #Define time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

os.system('modprobe w1-gpio')  
os.system('modprobe w1-therm')

#Gets the ID of temperature sensor
base_dir = '/sys/bus/w1/devices/' #Temperature serial code
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Opens folder for temperature sensor
def read_temp_raw(): #Define variable for raw temperature
    f = open(device_file, 'r') #Open, read, and record temperature file
    lines = f.readlines()
    f.close()
    return lines

#Reads the temperature coming from sensor
def read_temp():
    lines = read_temp_raw() #Grabs data from the temperature folder
    while lines[0].strip()[-3:] != 'YES': #Keeps on reading temperature for 'YES' signal
        time.sleep(0.2) #If it fails for 'YES' signal then it restarts
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=') #Find temperature output from sensor
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0 #Celsius temperature 
        temp_f = temp_c * 9.0 / 5.0 + 32.0 #Fahrenheit temp
        return temp_f  #Prints out temperature

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)

port = server_sock.getsockname()[1]

print "Waiting for connection on RFCOMM channel %d" % port 
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

while True:
	client_sock.send(str(int(read_temp())))
	print ("sending %s" % read_temp())	
client_sock.close()
server_sock.close()

