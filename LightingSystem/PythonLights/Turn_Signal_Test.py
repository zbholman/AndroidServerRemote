import time
from sense_hat import SenseHat

sense = SenseHat()
yellow = 255, 191, 0
sense.clear()

turn_signal = True
number_of_blinks = 5
for x in range(0, number_of_blinks):
    sense.set_pixel(7, 4, yellow)
    sense.set_pixel(7, 3, yellow)
    sense.set_pixel(6, 5, yellow)
    sense.set_pixel(6, 2, yellow)
    sense.set_pixel(5, 6, yellow)
    sense.set_pixel(5, 1, yellow)
    sense.set_pixel(4, 7, yellow)
    sense.set_pixel(4, 0, yellow)
   
    time.sleep(.5)
    sense.clear()
    time.sleep(.5)
