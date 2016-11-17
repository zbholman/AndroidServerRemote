nterface for incoming xBee messages, change this stuff based on your team.
#Written by Team 1
#Date: 11/14/2016
#Last Updated: 11/17/2016

'''
Notes
1. You may keep this as it's own file, or incorperate the code into your main codebase.
2. I reccomend puting this into your main code. 
3. You will have to edit this file to fit your specific system. We make sure you can get the message, you decide what you do with it.
'''

import serial
import sys
from threading import Thread

#Dictionary of acceptable messages
#Put your message codes in here, that way you can listen for them down below. Two examples provided. 
acceptedSources = {	
	'Breaking':1,
	'Lighting':2,
}

def listen():
	try:
		#Sets up serial port, listens for new lines to read.
		ser = serial.Serial('/dev/ttyUSB0', 9500)
		print('Listening')
	
		#Loop for message listening. Start in it's own thread.
		while True:
			incMsg = ser.readline().split()
			#Basic check, if the message is coming from the accepted sources, do your work.
			if incMsg == acceptedSources[1] or incMsg == acceptedSources[2]:
				doSomething()
	except(RuntimeError, OSError, ValueError, IOError) as e:
		print('Error:' + e)
		
#General function for your system work. 
#Here, you do some action based on the message.
def doSomething():
	pass

#Main function.
def main():
	try:
		#Creates a thread for message listening.
		listenThread = Thread(target=listen)
		listenThread.daemon = True
		listenThread.start()
	except(RuntimeError, OSError, ValueError, IOError) as e:
		print('Error:' + e)
		
if __name__ == '__main__':
	main()
