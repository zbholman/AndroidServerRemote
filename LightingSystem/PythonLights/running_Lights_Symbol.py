import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

green = (0, 255, 0)
turn_runningLight = True
number_of_blinks = 1
for x in range(0, number_of_blinks):
  sense.set_pixel(0, 2, green)
  sense.set_pixel(1, 2, green)
  sense.set_pixel(2, 2, green)
  sense.set_pixel(0, 4, green)
  sense.set_pixel(1, 4, green)
  sense.set_pixel(2, 4, green)
  sense.set_pixel(0, 6, green)
  sense.set_pixel(1, 6, green)
  sense.set_pixel(2, 6, green)
  sense.set_pixel(4, 1, green)
  sense.set_pixel(4, 2, green)
  sense.set_pixel(4, 3, green)
  sense.set_pixel(4, 4, green)
  sense.set_pixel(4, 5, green)
  sense.set_pixel(4, 6, green)
  sense.set_pixel(4, 7, green)
  sense.set_pixel(5, 1, green)
  sense.set_pixel(5, 7, green)
  sense.set_pixel(6, 2, green)
  sense.set_pixel(6, 6, green)
  sense.set_pixel(7, 3, green)
  sense.set_pixel(7, 4, green)
  sense.set_pixel(7, 5, green)
