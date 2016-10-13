  #Shivang Patel
  #10/03/2016
  #Displays speakers on sense hat. 

from sense_hat import SenseHat
import time

sense = SenseHat()

b = [0, 255, 0]
e = [0, 0, 0]

image = [
e,e,e,b,b,e,e,e,
e,e,b,e,e,b,e,e,
e,b,e,e,e,e,b,e,
b,e,e,b,b,e,e,b,
b,e,e,b,b,e,e,b,
e,b,e,e,e,e,b,e,
e,e,b,b,e,b,e,e,
e,e,e,b,b,e,e,e
]

sense.set_pixels(image)
time.sleep(3)

sense.show_message("Speaker On")
images = [speaker_on]
count = 0
i=0
while (i<3): 
   sense.set_pixels(images[count % len(images)]())
   time.sleep(.75)
   sense.clear()
   time.sleep(.75)
   sense.set_pixels(images[count % len(images)]())
   i+=1
