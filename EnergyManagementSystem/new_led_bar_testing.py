import time
from dotstar import Adafruit_DotStar

numpixels = 8

datapin = 16
clockpin = 20
strip = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()
strip.setBrightness(64)

#while True:
    
strip.setPixelColor(0, 255, 0, 0)
strip.setPixelColor(1, 255, 0, 0)
strip.setPixelColor(2, 255, 0, 0)
strip.setPixelColor(3, 255, 0, 0)
strip.setPixelColor(4, 255, 0, 0)
strip.setPixelColor(5, 255, 255, 0)
strip.setPixelColor(6, 255, 255, 0)
strip.setPixelColor(7, 0, 255, 0)
strip.show()

#except KeyboardInterrupt:
    #strip.setPixelColor(0, 0, 0, 0)
    #break
