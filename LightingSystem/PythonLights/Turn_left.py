from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

yellow = 255, 191, 0
turn_signal = True
number_of_blinks = 5
for i in range(0, number_of_blinks):
  for y in range(3, 4):
    for x in range(0, 8):
      sense.set_pixel(x, y, yellow)
      sense.set_pixel(x, (y+1), yellow)
      
  sense.set_pixel(3, 0, yellow)
  sense.set_pixel(2, 1, yellow)
  sense.set_pixel(3, 1, yellow)
  sense.set_pixel(3, 7, yellow)
  sense.set_pixel(3, 6, yellow)
  sense.set_pixel(3, 5, yellow)
  sense.set_pixel(2, 6, yellow)
  
  for x in range (1, 4):
    sense.set_pixel(x, 2, yellow)
  for x in range (1, 4):
    sense.set_pixel(x, 5, yellow)

  time.sleep(.5)
  sense.clear()
  time.sleep(.5)