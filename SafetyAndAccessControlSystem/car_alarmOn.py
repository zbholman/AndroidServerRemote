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
s.set_pixels(images[ 0 ]())

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
    ii = 0 
    tempPitch = 0
    tempRoll = 0
    tempYaw = 0
    if(abs(curPitch - newPitch) > 30):
        if(curPitch > 330 and newPitch < 30):
            tempPitch = newPitch + 360
            if(abs(tempPitch - curPitch) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(curPitch < 30 and newPitch > 330):
            tempPitch = curPitch + 360
            if(abs(tempPitch - newPitch) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(abs(curPitch - newPitch) > 30):
            print("before subP")
            subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
            print("after subP")
            ii = 1
            break
        #else:
            # Continue if the inner loop wasn't broken.
        #    sleep (0.03)
        #    continue
        
    if(abs(curRoll - newRoll) > 1):
        if(curRoll > 330 and newRoll < 30):
            tempRoll = newRoll + 360
            if(abs(tempRoll - curRoll) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(curRoll < 30 and newRoll > 330):
            tempRoll = curRoll + 360
            if(abs(tempRoll - newRoll) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(abs(curRoll - newRoll) > 30):
            print("before subP")
            subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
            print("after subP")
            ii = 1
            break
    
    if(abs(curYaw - newYaw) > 1):
        if(curYaw > 330 and newYaw < 30):
            tempYaw = newYaw + 360
            if(abs(tempYaw - curYaw) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(curYaw < 30 and newYaw > 330):
            tempYaw = curYaw + 360
            if(abs(tempYaw - newYaw) > 30):
                print("before subP")
                subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
                print("after subP")
                ii = 1
                break
        elif(abs(curYaw - newYaw) > 30):
            print("before subP")
            subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/car_alarmOff.py", shell=True)
            print("after subP")
            ii = 1
            break
            
    
    # Continue if the inner loop wasn't broken.
    if(ii == 0):
        time.sleep (0.03)
        continue
    else: # Inner loop was broken, break the outer.
        break

    
