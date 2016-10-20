from grovepi import grovepi
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.HIGH)

# --------- User Settings ---------
# The DHT_SENSOR_TYPE below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
DHT_SENSOR_TYPE = 1
# Connect the DHT sensor to one of the digital pins (i.e. 2, 3, 4, 7, or 8)
DHT_SENSOR_PIN = 3
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

   	
	if temp_f > 86:
		GPIO.output(4,GPIO.LOW)
		print "FAN ON"
	#	time.sleep(30);

	#	GPIO.cleanup()
		print "bye"
    except IOError:
        	print ("Error")

    		time.sleep(.10)

