 # Author: Ahmad Alhaddad, Yusef Savage 
 # Date: 11/8/2016 
 # Course: IST 440W 
 # Purpose: Turn off Fan Two 
 
 
 #import required Python libraries 
  import RPi.GPIO as GPIO
  import time
  import bluetooth
  import socket

 #create the socket object
    
   socket_client = bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 

 #Create host and port
   host = ''
   port = 1

   socket_client.connect((host, port)) 
   socket_client.send("FanTwoOn") 
 
 
 # Use BCM GPIO references instead of physical pin numbers 
 GPIO.setmode(GPIO.BCM) 
 
 
 # init list with pin numbers 
 

  pinList = [24] 
 
 
 # loop through pins and set mode and state to 'low' 
 
 
 for i in pinList:
     GPIO.setwarnings(False) 
     GPIO.setup(i, GPIO.OUT)  
     GPIO.output(i,0) 
 
 
 def trigger() : 
     for i in pinList:  
     GPIO.output(i,0) 
     break 

 try:  
     trigger() 
           
        
 except KeyboardInterrupt: 
    print "  Quit"  
    # Reset GPIO settings 
    GPIO.cleanup()
    FanTwoOnTOjson = {'Turn fan on'} 
    fileName = 'FanTwoOn.json' # name of the JSON output file 
    outFile = open(fileName, 'w') # W stands for writing, writing out to the JSON file 
    json.dump(FanTwoOnTOjson, outFile) # Dumping all contents from Temp to Json 
    client_sock.send(FanTwoOnTOjson) # Send JSON file over bluetooth connection 
    print ("sending [%s]" % FanTwoOnTOjson) # Print the contents of the JSON file being sent 
    outFile.close() # Close the outfile

 
 

   
            
