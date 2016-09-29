import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

yellow = 255, 191, 0
turn_hazrdLight = True
number_of_blinks = 100
for x in range(0, number_of_blinks):
  sense.set_pixel(0, 4, yellow)
  sense.set_pixel(1, 4, yellow)
  sense.set_pixel(1, 3, yellow)
  sense.set_pixel(2, 4, yellow)
  sense.set_pixel(2, 3, yellow)
  sense.set_pixel(2, 2, yellow)
  sense.set_pixel(3, 4, yellow)
  sense.set_pixel(3, 3, yellow)
  sense.set_pixel(3, 2, yellow)
  sense.set_pixel(3, 1, yellow)
  sense.set_pixel(4, 2, yellow)
  sense.set_pixel(4, 3, yellow)
  sense.set_pixel(4, 4, yellow)
  sense.set_pixel(5, 3, yellow)
  sense.set_pixel(5, 4, yellow)
  sense.set_pixel(6, 4, yellow)
  
  
  time.sleep(.5)
  sense.clear()
  time.sleep(.5)


user_word = input()

user_number = int(input())

print('%s,%d' % (user_word,user_number))
