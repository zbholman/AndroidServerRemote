# Author: Phuong Lu
# Date: 10/1/2016
# Course: IST 440W, Team 6
# Purpose: Detect car speed with accelerometer from Sense HAT

from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_accelerometer_raw()

print(sense.accelerometer)
