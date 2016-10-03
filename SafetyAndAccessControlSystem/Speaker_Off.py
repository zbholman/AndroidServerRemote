#Shivang Patel
#10/03/2016
#Displays speakes off on sense hat.


from sense_hat import SenseHat
import time

sense = SenseHat()

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

sense.set_pixels(image)
time.sleep(3)
sense.show_message("Speaker Off")
