#Shivang Patel
#10/03/2016
#Displays speakes off on sense hat.

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

b = [255, 0, 0]
e = [0, 0, 0]

image = [
e,e,e,b,b,e,e,b,
e,e,b,e,e,b,b,e,
e,b,e,e,e,b,b,e,
b,e,e,e,b,e,e,b,
b,e,e,b,e,e,e,b,
e,b,b,e,e,e,b,e,
e,b,b,b,e,b,e,e,
b,e,e,b,b,e,e,e
]

count = 0
i=0
while (i<3): 
   sense.set_pixels(image)
   time.sleep(.75)
   sense.clear()
   time.sleep(.75)
   sense.set_pixels(image)
   i+=1
