#GoPiGo Robot for DriveTrain
from gopigo import *
import sys

print('Welcome to the DriveTrain System')
print('Press:')
print('P or p to Park the Car')
print('R or r to Reverse the Car')
print('N or n to Neutral')
print('D or d to Drive the Car')
print('L or l to Move the Car Left')
print('R or r to Move the Car Right')
print('I or i to Increase the Speed')
print('E or e to Decrease the Speed')
print('Z or z to Exit the Drive Mode')

while True:
    print"Drive Mode:",
    mode = raw_input()
    if (mode == 'P' or 'p'):
        stop()  #Car In The Park Mode
    elif (mode == 'R' or 'r'):
        bwd() #Car Reversing
    elif (mode == 'N' or 'n'):
        stop()  #Car In The Neutral Mode
    elif (mode == 'D' or 'd'):
        fwd() #Car Moving Forward
    elif (mode == 'L' or 'l'):
        left() #Car Turning Left
    elif (mode == 'R' or 'r'):
        right() #Car Turning Right
    elif (mode == 'I' or 'i'):
        increase_speed() #Increasing The Car Speed
    elif (mode == 'E' or 'e'):
        decrease_speed() #Car Turning Left
    elif (mode == 'Z' or 'z'):
        print('Exiting Drive Mode') #Leaving Drive Mode
        sys.exit()
    else:
        print('Wrong Drive Mode Command, Please Try Again')
    time.sleep(.1)
    
        
        
    
        
    
        
    
    
    
