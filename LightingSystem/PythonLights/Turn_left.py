import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

yellow = 255, 191, 0
turn_signal = True
number_of_blinks = 5
for x in range(0, number_of_blinks):
    sense.set_pixel(0, 4, yellow)
    sense.set_pixel(0, 3, yellow)
    sense.set_pixel(1, 5, yellow)
    sense.set_pixel(1, 2, yellow)
    sense.set_pixel(2, 6, yellow)
    sense.set_pixel(2, 1, yellow)
    sense.set_pixel(3, 7, yellow)
    sense.set_pixel(3, 0, yellow)
    sense.set_pixel(7, 4, yellow)
    sense.set_pixel(7, 3, yellow)
    sense.set_pixel(6, 4, yellow)
    sense.set_pixel(6, 3, yellow)
    sense.set_pixel(5, 4, yellow)
    sense.set_pixel(5, 3, yellow)
    sense.set_pixel(4, 4, yellow)
    sense.set_pixel(4, 3, yellow)
    sense.set_pixel(3, 4, yellow)
    sense.set_pixel(3, 3, yellow)
    sense.set_pixel(2, 4, yellow)
    sense.set_pixel(2, 3, yellow)
    sense.set_pixel(1, 4, yellow)
    sense.set_pixel(1, 3, yellow)
    sense.set_pixel(2, 2, yellow)
    sense.set_pixel(2, 5, yellow)
    sense.set_pixel(3, 5, yellow)
    sense.set_pixel(3, 2, yellow)
    sense.set_pixel(3, 1, yellow)
    sense.set_pixel(3, 6, yellow)
    
    
    time.sleep(.5)
    sense.clear()
    time.sleep(.5)
