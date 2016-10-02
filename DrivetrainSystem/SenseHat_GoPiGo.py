#IST 440
# Drive Train (Team 02)
# Author: Ghansyam Patel
# Date: 09/30/2016
#GoPiGo Robot for DriveTrain
# GoPiGo + SenseHat

from gopigo import *
import sys
from sense_hat import SenseHat
from time import sleep

sense = SenseHat ()

#Displays the Start Up Screen
print('Welcome to the DriveTrain System')
print('Press:')
print('p to Park the Car')
print('r to Reverse the Car')
print('n to Neutral')
print('d to Drive the Car')
print('l to Move the Car Left')
print('r to Move the Car Right')
print('i to Increase the Speed')
print('e to Decrease the Speed')
print('z to Exit the Drive Mode')

car = '    ______'
car1= '  /___ __\\___'
car2= '   o-----o    '

while True:
    print"Drive Mode:",
    mode = raw_input()
    if (mode == 'p'):
        stop()  #Car In The Park Mode
        sense.show_letter("P", text_colour=[255, 0, 0]) #Red Color
    elif (mode == 'r'):
        bwd() #Car Reversing
        sense.show_letter("R", text_colour=[0, 255, 0]) #Green Color
    elif (mode == 'n'):
        stop()  #Car In The Neutral Mode
        sense.show_letter("N", text_colour=[0, 0, 255]) #Blue Color
    elif (mode == 'd'):
        fwd() #Car Moving Forward
        sense.show_letter("D", text_colour=[255, 0, 0]) #Red Color
    elif (mode == 'l'):
        left() #Car Turning Left
        sense.show_message("LEFT", text_colour=[255, 0, 0]) #Red Color
    elif (mode == 't'):
        right() #Car Turning Right
        sense.show_message("RIGHT", text_colour=[255, 0, 0]) #Red Color
    elif (mode == 'i'):
        increase_speed() #Increasing The Car Speed
        sense.show_message("INCREASE", text_colour=[0, 0, 255]) #Blue Color
    elif (mode == 'e'):
        decrease_speed() #Car Decreasing The Speed
        sense.show_message("DECREASE", text_colour=[255, 0, 0]) #Red Color
    elif (mode == 'z'):
        stop() #Car Stops before Exiting Drive Mode
        sense.show_message("EXITING", text_colour=[0, 255, 0]) #Green Color
        print('Exiting Drive Mode') #Leaving Drive Mode
        print(car) #Printing Car
        print(car1) #Printing Car
        print(car2) #Printing Car
        print('Good Bye!') #Exiting Message!
        sys.exit()
        sense.clear()
    else:
        print('Wrong Drive Mode Command, Please Try Again')
        sense.show_message("ERROR", text_colour=[0, 255, 0]) #Green Color
    time.sleep(.1)
