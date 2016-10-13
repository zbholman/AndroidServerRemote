#Ashish Baby
#Version 1.04
#10-13-16

from sense_hat import SenseHat
import time

s = SenseHat()
s.clear()
s.low_light = True

green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0,0,0)


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

while (i<3): 
   s.set_pixels(images[count % len(images)]())
   time.sleep(.75)
   s.clear()
   time.sleep(.75)
   s.set_pixels(images[count % len(images)]())
   i+=1
