#Ashish Baby
#Version 1.00
#10-1-16

from sense_hat import SenseHat
import time

s = SenseHat()
s.clear()
s.low_light = True

green = (0, 255, 0)
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
    
  

images = [doors_lock]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

