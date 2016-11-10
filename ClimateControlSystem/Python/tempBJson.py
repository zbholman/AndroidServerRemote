 # Author: Ahmad Alhaddad,Yousef Savage
 # Date: 11/8/2016 
 # Course: IST 440W 
 # Purpose: Check temperature sensor send from bluetooth to Android
 
 
 import os # Get the complete path of the current working directory 
 import glob # Return a possibly-empty list of path names 
 import time
 import bluetooth
 import socket
 
  #create the socket object
    
   socket_client = bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 

 #Create host and port
   host = ''
   port = 1

   socket_client.connect((host, port)) 
   socket_client.send(TempBJson)
   
 #Create folders for temperature sensor probe 
 os.system('modprobe w1-gpio')  
 os.system('modprobe w1-therm')
 
 
 #Gets the ID of temperature sensor 
   base_dir = '/sys/bus/w1/devices/' 
 device_folder = glob.glob(base_dir + '28*')[0] 
 device_file = device_folder + '/w1_slave' 
 
 
 #Opens folder for temperature sensor 
 def read_temp_raw(): 
     f = open(device_file, 'r') 
     lines = f.readlines() 
     f.close() 
     return lines 
 
 
 #Reads the temperature coming from sensor 
 def read_temp(): 
     lines = read_temp_raw() 
     while lines[0].strip()[-3:] != 'YES': 
         time.sleep(0.2) 
         lines = read_temp_raw() 
     equals_pos = lines[1].find('t=') 
     if equals_pos != -1: 
         temp_string = lines[1][equals_pos+2:] 
         temp_c = float(temp_string) / 1000.0 #Celsius temperature  
         temp_f = temp_c * 9.0 / 5.0 + 32.0 #Fahrenheit temperature 
         return temp_c, temp_f #Prints out temperature 
 	 
 #Continue to read temperature every second	 
 while True: 
 	print(read_temp())	 
 	time.sleep(1)

      # Reset GPIO settings 
    GPIO.cleanup()
    TempBJsonTOjson = {'Temp'} 
    fileName = 'TempBJson.json' # name of the JSON output file 
    outFile = open(fileName, 'w') # W stands for writing, writing out to the JSON file 
    json.dump(TempBJsonTOjson, outFile) # Dumping all contents from Temp to Json 
    client_sock.send(TempBJsonTOjson) # Send JSON file over bluetooth connection 
    print ("sending [%s]" % TempBJsonTOjson) # Print the contents of the JSON file being sent 
    outFile.close() # Close the outfile

