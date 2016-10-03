#andrew Rooney
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear() #clears previous image

turn_signal = True #Set turn_signal to true
number_of_blinks = 5 #gave the light 5 blinks
for x in range(0, number_of_blinks): #sets the lights pixel by pixel on the sense hat
    sense.set_pixel(7, 4, 255, 191, 0)
    sense.set_pixel(7, 3, 255, 191, 0)
    sense.set_pixel(6, 5, 255, 191, 0)
    sense.set_pixel(6, 2, 255, 191, 0)
    sense.set_pixel(5, 6, 255, 191, 0)
    sense.set_pixel(5, 1, 255, 191, 0)
    sense.set_pixel(4, 7, 255, 191, 0)
    sense.set_pixel(4, 0, 255, 191, 0)
    sense.set_pixel(0, 4, 255, 191, 0)
    sense.set_pixel(0, 3, 255, 191, 0)
    sense.set_pixel(1, 4, 255, 191, 0)
    sense.set_pixel(1, 3, 255, 191, 0)
    sense.set_pixel(2, 4, 255, 191, 0)
    sense.set_pixel(2, 3, 255, 191, 0)
    sense.set_pixel(3, 4, 255, 191, 0)
    sense.set_pixel(3, 3, 255, 191, 0)
    sense.set_pixel(4, 4, 255, 191, 0)
    sense.set_pixel(4, 3, 255, 191, 0)
    sense.set_pixel(5, 4, 255, 191, 0)
    sense.set_pixel(5, 3, 255, 191, 0)
    sense.set_pixel(6, 4, 255, 191, 0)
    sense.set_pixel(6, 3, 255, 191, 0)
    sense.set_pixel(5, 2, 255, 191, 0)
    sense.set_pixel(5, 5, 255, 191, 0)
    sense.set_pixel(4, 5, 255, 191, 0)
    sense.set_pixel(4, 2, 255, 191, 0)
    sense.set_pixel(4, 1, 255, 191, 0)
    sense.set_pixel(4, 6, 255, 191, 0)
    
    
    time.sleep(.5) #there is a .5 second timer between flashes
    sense.clear() #clears the sense hat
    time.sleep(.5) #another .5 second timer
