# Author: Phuong Lu
# Date: 10/1/2016
# Course: IST 440W - Team 6, Professor Oakes
# Purpose: Detect car speed with accelerometer from Sense HAT and display door lock/unlock functions based on speed

from sense_hat import SenseHat
#import pygame
import time
import subproccess

#Load door locking sound
#pygame.mixer.init()
#pygame.mixer.music.load("/home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/lockcar.wav")

#Get car speed from accelerometer
sense = SenseHat()
raw = sense.get_accelerometer_raw()

#Display speed
print(sense.accelerometer)

#Call display functions of locking/unlocking car if speed is over or under 5
if sense.accelerometer >= 5:
	subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/SenseHat/Doors_locked.py", shell=True)
	#pygame.mixer.music.play()
	time.sleep(5)
elif sense.accelerometer < 5:
	subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/SenseHat/Doors_unlock.py", shell=True)
