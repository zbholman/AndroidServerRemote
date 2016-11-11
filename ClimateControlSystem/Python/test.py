#! /usr/bin/env python3
import os
import RPi.GPIO as GPIO
import time
import datetime
import sys
from temp import read_temp
# 5 * * * * sudo python /home/pi/fan.py
# A crontab will run every hour and check the temp. If the temp is > 49 the script will start the fan
# until the temperature goes down to 28. When it does, the script will end, shutting down the fan as well.
# If the script executes again while a previous script is running, the latter will exit
# ... meaning the pi is in hell, and will never get bellow FAN_END value :P

# Identify which pin controls the relay
FAN_PIN = 23  # the yellow box ex: GPIO18
# Temperature check. Start fan if temp > 49C
FAN_START = 25
# Temperature check. Shut down under 28C
FAN_END = 26

# Get what action. If you manually turning on/off the fan
action = sys.argv.pop()


def GPIOsetup():
	GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(FAN_PIN, GPIO.OUT)
	
def fanON():
	GPIOsetup()
	GPIO.output(FAN_PIN, 0)	#fan on
	return()
def fanOFF():
	GPIOsetup()
	GPIO.output(FAN_PIN, 1)	#fan off
	return()
	
def get_temp_from_system():
	print(read_temp)
	return read_temp()
#	res = os.popen('vcgencmd measure_temp').readline()
#	return(res.replace("temp=","").replace("'C\n",""))

def check_fan(pin):
	GPIOsetup()
	return GPIO.input(pin)

def run(pin):
	current_date = datetime.datetime.now()
	temp = get_temp_from_system()
	if float(temp) >= FAN_START:
		print(temp+' @ '+str(current_date))
		if check_fan(pin) == 1:
			print('Fan is Off...Starting Fan')
			fanON()
		else:
			time.sleep(5) # Remove, if you want real-time checking
			print('Fan is ON')
	elif float(temp) <= FAN_END:
		print(temp+' @ '+str(current_date))
		if check_fan(pin) == 0:
			print('Fan is on...Shuting it Down')
			fanOFF()
			GPIO.cleanup()
			return 1 # exit script. The pi has cooled down
		else:
			time.sleep(5) # Remove, if you want real-time checking
			print('Fan is OFF')
	else:
			pass # while the script is passing through here, there will be no output on screen
			
			
if action == "on" :
   print "Turning fan on"
   fanON()
elif action == "off" :
   print "Turning fan off"
   fanOFF()

# first check if script is already running
if check_fan(FAN_PIN) == 0:
	print('Fan is on, script must be running from another instance...')
	print (read_temp)
else:
	temp = get_temp_from_system()
	if float(temp) < FAN_START:
		print('Pi is operating under normal temperatures.')
	else:
		try:
			while(True):
				tmp = run(FAN_PIN)
				if tmp == 1: # value returned from line 60
					break
		except KeyboardInterrupt:
			fanOFF()
			GPIO.cleanup()
		finally:
			fanOFF()
			GPIO.cleanup()
