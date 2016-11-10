#Matt Handwerk
#IST 440W Fall 2016
#PennState Abington
#Professor Oakes
#Version 1.04
#Creates image on sense hat indicating that the car doors are locked
#11-10-16

//Imports for sensehat and time for frequency
from sense_hat import SenseHat
import time
sense = SenseHat()

//Gets and prints current orientations
while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
  
    //Rounds orientation values to nearest whole number
    pitch = round(pitch, 1)
    roll = round(roll, 1)
    yaw = round(yaw, 1)

    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
