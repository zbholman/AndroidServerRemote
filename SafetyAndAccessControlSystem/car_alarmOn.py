# Contributors: Phuong Lu, Joey Lee, and Matt Handwerk
# Date: 10/4/2016
# Course: IST 440W - Team 6, Professor Oakes
# Purpose: Display car alarm logo on Sense HAT when alarm is turned on

from sense_hat import SenseHat
import time
import pygame
import set_alarmOff
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
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    if(pitch < 10):
        tempPitch = pitch + 360
    else:
        tempPitch = pitch
      
    if(roll < 10):
        tempRoll =  roll + 360
    else:
        tempRoll = roll
      
    if(yaw < 10):
        tempYaw = yaw + 360
    else:
        tempYaw = yaw
      
    #Checks values to see if a 3 point change in any axis has occurred
    if((abs(curPitch - pitch) > 9) or (abs(curRoll - roll) > 9) or (abs(curYaw - yaw) > 9) or (abs(curPitch - tempPitch) > 9) or (abs(curRoll - tempRoll) > 9) or (abs(curYaw - tempYaw) > 9)):
        subprocess.Popen("set_alarmOff.py", shell=True)
            break
    else:
        # Continue if the inner loop wasn't broken.
        sleep (0.03)
        continue
    # Inner loop was broken, break the outer.
    break

    
