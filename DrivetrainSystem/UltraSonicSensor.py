#IST 440 
# Drive Train (Team 02) 
# Author: Ghansyam Patel, Rahul Manoharan, and Klaus Herchenroder
# Date: 10/03/2016
# GoPiGo Robot for DriveTrain
# UltraSonic Sensor Python Code
from gopigo import * 
import sys 
import time

#UltraSonice Sensor to be connected on Port A01 on the Pi
#Distance from obstacle where the GoPiGo should stop
distance_to_stop=20
 
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
       print('Drive Mode:')
       dist=us_dist(15) #Find the distance of the object in front
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
           stop() #Car Stops before Exiting Drive Mode 
           print('Exiting Drive Mode') #Leaving Drive Mode 
           print(car) #Printing Car 
           print(car1) #Printing Car 
           print(car2) #Printing Car 
           print('Good Bye!') #Exiting Message! 
           sys.exit()

       elif dist<distance_to_stop:
	       stop()	
	       break 

       else:
           print('Wrong Drive Mode Command, Please Try Again') 
       time.sleep(.1) 

