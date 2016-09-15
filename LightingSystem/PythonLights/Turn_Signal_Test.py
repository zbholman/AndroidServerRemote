import time
from sense_hat import SenseHat

sense = SenseHat()
yellow = 255, 191, 0
sense.clear()

turn_signal = True
number_of_blinks = 5
for x in range(0, number_of_blinks):
<<<<<<< HEAD
    sense.set_pixel(7, 4, 255, 191, 0)
    sense.set_pixel(6, 4, 255, 191, 0)
    sense.set_pixel(7, 3, 255, 191, 0)
    sense.set_pixel(6, 5, 255, 191, 0)
    sense.set_pixel(6, 2, 255, 191, 0)
    sense.set_pixel(5, 6, 255, 191, 0)
    sense.set_pixel(5, 1, 255, 191, 0)
    sense.set_pixel(4, 7, 255, 191, 0)
    sense.set_pixel(4, 0, 255, 191, 0)
    sense.set_pixel (0, 4, 255, 191, 0)
    sense.set_pixel(0, 3, 255, 191, 0)

=======
    sense.set_pixel(7, 4, yellow)
    sense.set_pixel(7, 3, yellow)
    sense.set_pixel(6, 5, yellow)
    sense.set_pixel(6, 2, yellow)
    sense.set_pixel(5, 6, yellow)
    sense.set_pixel(5, 1, yellow)
    sense.set_pixel(4, 7, yellow)
    sense.set_pixel(4, 0, yellow)
>>>>>>> dc3a912b03e6a147649a9e1eeeeaa50b4990664d
   
    time.sleep(.5)
    sense.clear()
    time.sleep(.5)
