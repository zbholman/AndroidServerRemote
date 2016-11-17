# Contributors: Phuong Lu, Joey Lee, and Matt Handwerk
# Date: 10/4/2016
# Course: IST 440W - Team 6, Professor Oakes
# Purpose: Display car alarm logo on Sense HAT when alarm is turned on

from sense_hat import SenseHat
import time
import pygame
import subprocess

#pygame.mixer.init()
#pygame.mixer.music.load("setalarm.mp3")
#pygame.mixer.music.play()

s = SenseHat()
s.clear()
s.low_light = True

green = (0, 0, 0)
red = (0, 0, 0)
blue = (0, 0, 255)
nothing = (0, 0, 0)

def car_alarm():
  B = blue
  O = nothing
  logo = [
    O, O, O, O, O, O, O, O,
    O, B, B, B, B, B, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, O, B, B, O, B, O, O,
    O, O, O, B, B, O, O, O,
    ]
  return logo
    
images = [car_alarm]
s.set_pixels(images[count % len(images)]())

#Sets initial orientations
curOri = s.get_orientation()
curPitch = curOri["pitch"]
curRoll = curOri["roll"]
curYaw = curOri["yaw"]

#With a frequency of 30ms, checks current orientation to check for Impact
while True:
    o = s.get_orientation()
    newPitch = o["pitch"]
    newRoll = o["roll"]
    newYaw = o["yaw"]
    
    tempPitch = 0
    tempRoll = 0
    tempYaw = 0
    if(abs(curPitch - newPitch) > 5):
        if(curPitch > 330 and newPitch < 30):
            tempPitch = newPitch + 360
            if(abs(tempPitch - curPitch) > 5):
                subprocess.Popen("usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/set_alarmOff.py", shell=True)
                break
        elsif(curPitch < 30 and newPitch > 330):
            tempPitch = curPitch + 360
            if(abs(tempPitch - newPitch) > 5):
                subprocess.Popen("usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/set_alarmOff.py", shell=True)
                break
        elsif(abs(curYaw - newYaw) > 5):
            subprocess.Popen("usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/set_alarmOff.py", shell=True)
            break
        else:
            # Continue if the inner loop wasn't broken.
            sleep (0.03)
            continue
    else:
        # Continue if the inner loop wasn't broken.
        sleep (0.03)
        continue
    # Inner loop was broken, break the outer.
    break

    
