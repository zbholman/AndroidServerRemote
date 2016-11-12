import json
import pyowm #Python Open Weather Map
import bluetooth # Python bluetooth tools 

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
bluetooth.advertise_service(server_sock, "nexus", uuid)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()

try:
# Register API Key with source
 API_key = '89cb9b3c8c3c1ee033be08ffcfd26076'
 owm = pyowm.OWM(API_key)

# Register a location: city,state AND print
 location = 'Philadelphia,PA'
 print('Location:', location)

# Find a location to observe outdoor weather
 obs = owm.weather_at_place(location)
 w = obs.get_weather()

# Check outdoor Fahrenheit temperature and print
 outdoorFahrenheit = w.get_temperature('fahrenheit')
 print('Fahrenheit:', outdoorFahrenheit['temp'])

# Check outdoor Humidity percentage and print
 outdoorHumidity = w.get_humidity()
 print('Humidity:', outdoorHumidity, '%')

while True:
 
	print "Waiting for connection on RFCOMM channel %d" % port

	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info

 data = client_sock.recv(1024)
 if len(data) == 0: break
	 print "received [%s]" % data
	if data == 'temp'
		data = outdoorFahrenheit
   
except IOError:
 print("Error")
