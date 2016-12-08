import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

padPin=18
GPIO.setup(padPin,GPIO.IN)

while True:
    padPressed = GPIO.input(padPin)

    if padPressed:
        subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/SenseHat/Doors_unlock.py", shell=True)
    time.sleep(0.5)
