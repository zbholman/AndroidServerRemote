import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

yellow = 255, 191, 0
turn_runningLight = True
number_of_blinks = 1
for x in range(0, number_of_blinks):
  sense.set_pixel(1, 0, yellow)
  sense.set_pixel(1, 1, yellow)
  sense.set_pixel(2, 0, yellow)
  sense.set_pixel(2, 1, yellow)
  sense.set_pixel(5, 0, yellow)
  sense.set_pixel(5, 1, yellow)
  sense.set_pixel(6, 0, yellow)
  sense.set_pixel(6, 1, yellow)
