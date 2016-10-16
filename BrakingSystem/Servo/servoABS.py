import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7)

while(1)
    for i in range(0,90):
        DC=1./18.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(.01)
    for i in range(90,0,-1):
        DC=1/18.*(i) + 2
        pwm.ChangeDutyCycle(DC)
        time.sleep(.01)
pwm.stop()
GPIO.cleanup()
