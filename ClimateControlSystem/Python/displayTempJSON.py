#Class: IST440W 
#Professor: Joe Oakes
#Team 3
#Authors: Mohammed, Ahmad

from grovepi import grovepi
import os
import time

# --------- User Settings ---------
# The DHT_SENSOR_TYPE below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
DHT_SENSOR_TYPE = 1
# Connect the DHT sensor to one of the digital pins (i.e. 2, 3, 4, 7, or 8)
DHT_SENSOR_PIN = 4
CONVERT_TO_FAHRENHEIT = True
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


while True:
    try:
        [temp_c,hum] = grovepi.dht(DHT_SENSOR_PIN,DHT_SENSOR_TYPE)
        if isFloat(temp_c):
                if (CONVERT_TO_FAHRENHEIT):
                        temp_f = temp_c * 9.0 / 5.0 + 32.0
                        print "Temperature(F):", temp_f
                else:
                        print "Temperature(C):", temp_c

        if ((isFloat(hum)) and (hum >= 0)):
                print "Humidity(%):", hum
                
# Create a dictionary object for gathering all data from temperature sensor to write out to a JSON file
    tempTOjson = {'temp': temp_f, 'humidity': hum}

    fileName = 'displayTemp.json'# name of the JSON output file
    outFile = open(fileName, 'w')#W stands for writing, writing out to JSON file
    json.dump(tempTOjson, outFile)#Dumping all contents from Temp to Json
    outFile.close()#Close the outfile
    except IOError:
        print ("Error")

    time.sleep(5)
