#IST 440
# Drive Train (Team 02)
# Author: Ghansyam Patel, Rahul Manoharan, and Klaus 
# Version: 1.02
# Date: 09/30/2016
#GoPiGo Robot for DriveTrain

#Unit tests added by Klaus Herchenroder
from gopigo import *
import sys

#Import Unit Test
import unittest

#Returns Value True
def IsTrue():
	return True
    
#Returns p indicating car is in park
def InPark():
    return 'p'

#Returns r indicating car is in reverse
def InReverse():
    return 'r'

#Returns n indicating car is in neutral
def InNeutral():
    return 'n'

#Returns z indicating car is stoping
def Stop():
    return 'z'

class IsRunning():
    
    #Checks if return value is true
    def TrueTest(self):
        self.assertTrue(IsTrue())

    #Checks if car is in park
    def ParkTest(self):
        self.assertEqual(InPark(), mode)

    #Checks if car is in reverse
    def ReverseTest(self):
        self.assertEqual(InReverse(), mode)

    #Checks if car is in neutral
    def NeutralTest(self):
        self.assertEqual(InNeutral(), mode)

    #Checks if car is stoping
    def StopTest(self):
        self.assertEqual(Stop(), mode)

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
car2= ' /___________ /'
car3= '  O----------O'

#Unit test for code is running
if TrueTest():
    #While car is running
    while True:
            print('Drive Mode:')
            mode = raw_input()
            if (mode == 'p'):
                    #Tests if the car is recieveing park input
                    if ParkTest():
                        stop()  #Car In The Park Mode
            elif (mode == 'r'):
                    #Tests if the car is recieveing reverse input
                    if ReverseTest(): 
                        bwd() #Car Reversing
            elif (mode == 'n'):
                    #Tests if the car is recieveing neutral input
                    if NeutralTest(): 
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
                    #Tests if the car is recieveing stop input
                    if StopTest():
                        stop() #Car Stops before Exiting Drive Mode
                        print('Exiting Drive Mode') #Leaving Drive Mode
                        print(car) #Printing Car
                        print(car1) #Printing Car
                        print(car2) #Printing Car
                        print('Good Bye!') #Exiting Message!
                        sys.exit()
            else:
                #Prints message if no mode exists for input
                print('Wrong Drive Mode Command, Please Try Again')
            time.sleep(.1)


if __name__ == '__main__':
    unittest.main()
