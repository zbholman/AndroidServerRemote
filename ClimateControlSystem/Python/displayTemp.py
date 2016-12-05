#IST 440 Penn State Abington
#Professor: Joseph Oakes
#Fall 2016
#Controller.py
#Author: Nirav Patel

# displayTemp.py reads the tempertaure from the sensor which is attached to raspberry pi and sends the data to client
# via Bluetooth Socket connection.It also read the outside temperature and humidity through a API and sends that infomation
# to client which is android tablet.

import bluetooth # for bluetooth connnection
import time # to keep performing some function at time intervals.
import os #Enable wire drivers and interface with sensor
import glob #Load drivers
import time #Define time
import pyowm # API for outside temp and humidity.


# Setting the locaation and API key fro outside weather.
API_key = '89cb9b3c8c3c1ee033be08ffcfd26076'
owm = pyowm.OWM(API_key)
# Register a location: city,state AND print
location = 'Philadelphia,PA'
 # Find a location to observe outdoor weather
obs = owm.weather_at_place(location)
w = obs.get_weather()

#inside function for temperature sensor which is attached to gpio pin 4.
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

#Reads the Exterior temperature from weather API
def exterior_temp():
        # Check outdoor Fahrenheit temperature and print
        outdoorFahrenheit = w.get_temperature('fahrenheit')
        return outdoorFahrenheit['temp'] # retuns exterior temp
    
#Reads the humidity from weather API
def humidity():
        # Check outdoor Humidity percentage and print
        outdoorHumidity = w.get_humidity()
        return outdoorHumidity # returns humidity

# Server socket creation using Bluetooth Socket on Port 2.
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)

port = server_sock.getsockname()[1]

#Server waiting for client to join on port 2
print "Waiting for connection on RFCOMM channel %d" % port 
client_sock, client_info = server_sock.accept()
print "Accepted connection from ", client_info

#loop
while True:
	# Server sends the sensor temp, outside temp and humidity to client.
	client_sock.send((str(int(read_temp()))) + " " + (str(int(exterior_temp())))+ " " + (str(int(humidity()))))
	print ("Sending : Sensor Temp: %s , Exterior Temp: %s ,Humidity: %s" % (read_temp(),exterior_temp(),humidity()))

	#closing the server and client connection.
client_sock.close()
server_sock.close()

