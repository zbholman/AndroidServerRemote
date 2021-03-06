#IST 440
# Drive Train (Team 02)
# Author: LaQuelle Martin
# Date: 10/10/2016
#Sense Hat accelerometer provides the amount of gravitational force that acts on each axis 

from sense_hat import SenseHat

sense = SenseHat()

#Gets the amount of gravitational acceleration for each x, y, and z axis from the accelerometer

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

#Rounds axis data to the nearest whole number

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

#Displays axis data which represents the acceleration intensity of the axis
    print("x={0}, y={1}, z={2}".format(x, y, z))
