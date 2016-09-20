from grovepi import *
from grove_rgb_lcd import *

ultrasonic_ranger = 4  # Insert ultrasonic_ranger to D4

while True:
    try:
        # Read distance value from Ultrasonic
        distant = ultrasonicRead(ultrasonic_ranger)
        d = str(distant)
        if distant <= 10:
            setRGB(0,128,64)
            setRGB(0,255,0)
            setText("STOP!!! " + d + "cm")
        elif distant <= 15:
            setText("Getting a little too Close " + d + " cm")
        else:
            setText("Dist = " + d + " cm")

    except TypeError:
        print("Error")
        setText("Error")
    except IOError:
        print("Error")
        setText("Error")
