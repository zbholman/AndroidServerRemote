#Andrew Rooney
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear() #clears prevous sense hat image

seatbeltlight = True

if (seatbeltlight == True): #sets seatbelt light to true, places pixel on given spot.
    
    sense.set_pixel(2, 7, 255, 0, 0)
    sense.set_pixel(5, 7, 255, 0, 0)
    sense.set_pixel(2, 6, 255, 0, 0)
    sense.set_pixel(5, 6, 255, 0, 0)
    sense.set_pixel(3, 6, 255, 0, 0)
    sense.set_pixel(4, 6, 255, 0, 0)
    sense.set_pixel(2, 5, 128, 128, 128)
    sense.set_pixel(5, 5, 128, 128, 128)
    sense.set_pixel(4, 5, 128, 128, 128)
    sense.set_pixel(3, 5, 128, 128, 128)
    sense.set_pixel(5, 4, 255, 0, 0)
    sense.set_pixel(4, 4, 255, 0, 0)
    sense.set_pixel(3, 4, 255, 0, 0)
    sense.set_pixel(2, 4, 255, 0, 0)
    sense.set_pixel(2, 3, 255, 0, 0)
    sense.set_pixel(3, 3, 255, 0, 0)
    sense.set_pixel(4, 3, 255, 0, 0)
    sense.set_pixel(5, 3, 255, 0, 0)
    sense.set_pixel(3, 2, 255, 0, 0)
    sense.set_pixel(4, 2, 255, 0, 0)
    sense.set_pixel(2, 1, 255, 0, 0)
    sense.set_pixel(3, 1, 255, 0, 0)
    sense.set_pixel(4, 1, 255, 0, 0)
    sense.set_pixel(5, 1, 255, 0, 0)   
    sense.set_pixel(2, 0, 255, 0, 0)
    sense.set_pixel(3, 0, 255, 0, 0)
    sense.set_pixel(4, 0, 255, 0, 0)
    sense.set_pixel(5, 0, 255, 0, 0)
    sense.set_pixel(5, 0, 255, 0, 0)
    sense.set_pixel(5, 0, 255, 0, 0)
    sense.set_pixel(0, 6, 128, 128, 128)
    sense.set_pixel(1, 5, 128, 128, 128)
    sense.set_pixel(3, 4, 128, 128, 128)
    sense.set_pixel(4, 3, 128, 128, 128)
    sense.set_pixel(5, 2, 128, 128, 128)
    sense.set_pixel(6, 1, 128, 128, 128)
    sense.set_pixel(7, 0, 128, 128, 128)
    sense.set_pixel(6, 5, 128, 128, 128)
    sense.set_pixel(7, 6, 128, 128, 128)
     
