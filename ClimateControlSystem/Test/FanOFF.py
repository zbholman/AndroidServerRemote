#Ahmad Alhaddad
#Fan OFF



def GPIOsetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    GPIO.setwarnings(False)

def fanOFF():
    GPIO.output(FAN_PIN, 1)
    print("fan off")
    return()

def main():
    GPIOsetup()
    getTEMP()

try:
    main()
finally:
    print ("Finish")
    #GPIO.cleanup()

fanOFF()

