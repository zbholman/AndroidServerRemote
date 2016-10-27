
#Ashish Baby
#IST 440W Fall 2016
#PennState Abington
#Professor Oakes
#Version 1.04
#Creates image on sense hat indicating that the car doors are unlocked
#10-13-16

from sense_hat import SenseHat
import time

import pygame #python module

pygame.mixer.init()
pygame.mixer.music.load("unlockcar.wav")
pygame.mixer.music.play()

s = SenseHat()
s.clear() #clears whatever is on sense hat
s.low_light = True

#Tells sense hat what colors are going to be used 
green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0,0,0)

#aranges whenre each colored pixel will be to create picture
def doors_unlock():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    G, G, G, G, G, G, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, O, O, O, O, O, G, O,
    G, G, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
  

images = [doors_unlock]
count = 0

i=0

#picture will blink three times before becoming still
while (i<3): 
   s.set_pixels(images[count % len(images)]())
   time.sleep(.75)
   s.clear()
   time.sleep(.75)
   s.set_pixels(images[count % len(images)]())
   i+=1
