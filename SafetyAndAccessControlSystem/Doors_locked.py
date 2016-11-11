#Ashish Baby
#IST 440W Fall 2016
#PennState Abington
#Professor Oakes
#Version 1.04
#Creates image on sense hat indicating that the car doors are locked
#10-13-16


from sense_hat import SenseHat
import time

import pygame #python module

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/lockcar.wav")
pygame.mixer.music.play()

s = SenseHat()
s.clear() #clears previous sense hat image
s.low_light = True
green = (0, 255, 0) #teling the sense what colors are going to be 
red = (255, 0, 0)
nothing = (0,0,0)


def doors_lock():
  R = red
  O = nothing
  logo = [
    R, O, O, O, O, O, O, R,
    O, R, O, O, O, O, R, O,
    O, O, R, O, O, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, R, O, O, R, O, O,
    O, R, O, O, O, O, R, O,
    R, O, O, O, O, O, O, R,
    ]
  return logo
    #mapping out how the pixels and different colors will be arranged
  

images = [doors_lock]
count = 0

s.set_pixels(images[count % len(images)]())
time.sleep(.75)
