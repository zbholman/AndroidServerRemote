import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

turn_signal = True
number_of_blinks = 5
for x in range(0, number_of_blinks):
    sense.set_pixel(0, 4, 255, 191, 0)
    sense.set_pixel(0, 3, 255, 191, 0)
    sense.set_pixel(1, 5, 255, 191, 0)
    sense.set_pixel(1, 2, 255, 191, 0)
    sense.set_pixel(2, 6, 255, 191, 0)
    sense.set_pixel(2, 1, 255, 191, 0)
    sense.set_pixel(3, 7, 255, 191, 0)
    sense.set_pixel(3, 0, 255, 191, 0)
    sense.set_pixel(7, 4, 255, 191, 0)
    sense.set_pixel(7, 3, 255, 191, 0)
    sense.set_pixel(6, 4, 255, 191, 0)
    sense.set_pixel(6, 3, 255, 191, 0)
    sense.set_pixel(5, 4, 255, 191, 0)
    sense.set_pixel(5, 3, 255, 191, 0)
    sense.set_pixel(4, 4, 255, 191, 0)
    sense.set_pixel(4, 3, 255, 191, 0)
    sense.set_pixel(3, 4, 255, 191, 0)
    sense.set_pixel(3, 3, 255, 191, 0)
    sense.set_pixel(2, 4, 255, 191, 0)
    sense.set_pixel(2, 3, 255, 191, 0)
    sense.set_pixel(1, 4, 255, 191, 0)
    sense.set_pixel(1, 3, 255, 191, 0)
    sense.set_pixel(2, 2, 255, 191, 0)
    sense.set_pixel(2, 5, 255, 191, 0)
    sense.set_pixel(3, 5, 255, 191, 0)
    sense.set_pixel(3, 2, 255, 191, 0)
    sense.set_pixel(3, 1, 255, 191, 0)
    sense.set_pixel(3, 6, 255, 191, 0)
    
    
    time.sleep(.5)
    sense.clear()
    time.sleep(.5)
