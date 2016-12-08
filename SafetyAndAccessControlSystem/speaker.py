import wiringpi
import time

print wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(22,1)
wiringpi.softToneCreate(22)

while True:
    wiringpi.softToneWrite(22,800)
    time.sleep(.1)
    wiringpi.softToneWrite(22,100)
    time.sleep(.1)

