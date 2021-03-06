#IST 440
# Drive Train (Team 02)
# Author: Ghansyam Patel
# Date: 09/30/2016
#Sense Hat
#GoPiGo Robot for DriveTrain

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#Prints Message for each Drive Mode the Car is in
sense.show_message("PARK",text_colour=[255, 0, 0]) #Red Color
sleep(1)
sense.show_message("REVERSE",text_colour=[0, 0, 255]) #Green Color
sleep(1)
sense.show_message("NEUTRAL",text_colour=[0, 255, 0]) #Blue Color
sleep(1)
sense.show_message("DRIVE",text_colour=[255, 0, 0])
sleep(1)
sense.show_message("LEFT",text_colour=[0, 0, 255])
sleep(1)
sense.show_message("RIGHT",text_colour=[0, 255, 0])
sleep(1)
sense.show_message("Increase",text_colour=[255, 0, 0])
sleep(1)
sense.show_message("Decrease",text_colour=[0, 0, 255])
sleep(1)
sense.show_message("Exiting",text_colour=[0, 255, 0])
sleep(1)
sense.clear() 
