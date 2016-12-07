#Ashish Baby
#IST 440W Fall 2016
#PennState Abington
#Professor Oakes
#10-4-16

from sense_hat import SenseHat
import time

s = SenseHat()
s.clear()
s.low_light = True

green = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 0)
nothing = (0, 0, 0)

number_blinks = 10

def car_alarmOff():
  for x in range(0, number_blinks):
    R = red
    O = nothing
    logo = [
      O, O, O, O, O, O, O, O,
      O, R, R, R, R, R, R, O,
      O, R, R, R, O, O, R, O,
      O, R, R, R, O, O, R, O,
      O, R, R, R, O, O, R, O,
      O, R, R, R, O, O, R, O,
      O, O, R, R, O, R, O, O,
      O, O, O, R, R, O, O, O,
      ]
    
    s.clear()
    time.sleep(.3)
    return logo
    
    
  
images = [car_alarmOff]
count = 0

while count<3:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
