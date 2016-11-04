import json
import pyowm #Python Open Weather Map
import bluetooth

#Bluetooth hexidecimal address of Raspberry Pi device
bd_addr = "50:46:5D:1D:00:4C"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

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

# Create a dictionary object for gathering all data from PYOWM to write out to a JSON file
 outdoorTempTOjson = {'Location': location, 'Fahrenheit temperature': outdoorFahrenheit, 'Humidity': outdoorHumidity}
 fileName = 'outdoorWeather.json' # name of the JSON output file
 outFile = open(fileName, 'w') # W stands for writing, writing out to the JSON file
 json.dump(outdoorTempTOjson, outFile) # Dumping all contents from Temp to Json
sock.send(outdoorTempTOjson)
 print ("sending [%s]" % outdoorTempTOjson)
 outFile.close() # Close the outfile

except IOError:
 print("Error")
 
 sock.close()
