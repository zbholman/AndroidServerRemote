#GoPiGo Robot for DriveTrain
from gopigo import *
import sys

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

while True:
    print"Drive Mode:",
    mode = raw_input()
    if (mode == 'p'):
        stop()  #Car In The Park Mode
    elif (mode == 'r'):
        bwd() #Car Reversing
    elif (mode == 'n'):
        stop()  #Car In The Neutral Mode
    elif (mode == 'd'):
        fwd() #Car Moving Forward
    elif (mode == 'l'):
        left() #Car Turning Left
    elif (mode == 't'):
        right() #Car Turning Right
    elif (mode == 'i'):
        increase_speed() #Increasing The Car Speed
    elif (mode == 'e'):
        decrease_speed() #Car Turning Left
    elif (mode == 'z'):
        print('Exiting Drive Mode') #Leaving Drive Mode
        sys.exit()
    else:
        print('Wrong Drive Mode Command, Please Try Again')
    time.sleep(.1)
    
        
        
    
        
    
        
    
    
    
