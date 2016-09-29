
import grovepi
sensor = 4

try:
        [temp,humidity] = grovepi.dht(sensor,1)
        print temp 

except IOError:
        print "Error"
