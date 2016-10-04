from sense_hat import SenseHat
import time

s = SenseHat()
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
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
