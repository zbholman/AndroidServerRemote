import grovepi
import math
import decimal

#Connect sensor to port D4

sensor = 4 #set which port is being used

while True:
  try:
      [temp,humidity] = grovepi.dht(sensor,1) #Checks if the sensor is in the right port
      temp = round(temp * 9/5 + 32.1) #temperature conversion from Celsius to Fahrenheit
      print "temp =", temp, "F/thumidity =", humidity,"%"
      t = str(temp)
      h = str(humidity)

  except IOError:
        print "Error"
