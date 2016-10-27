import json
import pyowm #Python Open Weather Map
from bluetooth import * # Python bluetooth tools 

server_sock= BluetoothSocket( RFCOMM ) 
server_sock.bind(("",PORT_ANY)) 
server_sock.listen(1) 
 
 
port = server_sock.getsockname()[1] 
 
 
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ])

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
 client_sock.send(outdoorTempTOjson) # Send JSON file over bluetooth connection
 print ("sending [%s]" % outdoorTempTOjson) # Print the contents of the JSON file being sent
 outFile.close() # Close the outfile

except IOError:
 print("Error")
