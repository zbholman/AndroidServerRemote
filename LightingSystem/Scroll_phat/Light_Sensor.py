import time
import grovepi
import running_lights #delete these files. No longer needed. 
import high_beams #delete these files. No longer needed.
import scrollphat

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

highBeam = False
lowBeam = False

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        if resistance > sensor_value:

            scrollphat.set_brightness(500)
            #go through columns then rows, turning all pixels on
            for y in range(5):
                 for x in range(11):
                      scrollphat.set_pixel(x,y,True)
                      scrollphat.update()
 
        else:

	    
            scrollphat.set_brightness(20)
            #go through columns then rows, turning all pixels on
            for y in range(5):
                 for x in range(11):
                      scrollphat.set_pixel(x,y,True)
                      scrollphat.update()
	

    except IOError:
        print ("Error")

