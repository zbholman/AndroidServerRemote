import RPi.GPIO as GPIO
import time
from grovepi import grovepi

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [4]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 10

# main loop
DHT_SENSOR_TYPE = 1
DHT_SENSOR_PIN = 3

try:
  
  [temp_c,hum] = grovepi.dht(DHT_SENSOR_PIN,DHT_SENSOR_TYPE)
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  
  if temp_f > 70:
        GPIO.output(4,GPIO.LOW)
  	print "Fan ON"
        time.sleep(30);	
 
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
