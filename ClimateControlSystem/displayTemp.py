import grovepi
	
	sensor = 4  
	blue = 0    # The Blue colored sensor.
	white = 1   # The White colored sensor.
	

	while True:
	    try:
	        [temp,humidity] = grovepi.dht(sensor,blue)  
	        print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	    except IOError:
	        print ("Error")

