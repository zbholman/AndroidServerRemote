#IST440
#Climate Control
#Ahmad Alhaddad
#10/23/2016
#Fan ON

#General Purpose input/output
def GPIOsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.setwarnings(False)
#Turns the fan on 
def fanON() -> object: #
    GPIO.output(FAN_PIN, 0)#Pin means fan is on 
    print("fan on")#It displays that the fan is on
    return()

#turns fan on
fanON()
