#Ahmad Alhaddad
#Fan ON



def GPIOsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.setwarnings(False)

def fanON(): #
    GPIO.output(FAN_PIN, 0)
    print("fan on")
    return()

def main():
    GPIOsetup()
    getTEMP()

try:
    main()
finally:
    print ("Finish")
    #GPIO.cleanup()

fanON()

