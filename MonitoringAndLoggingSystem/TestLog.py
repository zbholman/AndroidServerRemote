'''	TestLog.py
	Author: Ion Sirotkin
	10/27/2016
	IST 411 Team 02 Monitoring and Logging
	Version 1
	Purpose: To test the Logging class to ensure that a message can come in, and the
                 message will be stored in the correct collections.
'''

#Import the message and log class
from Message import Message
from logging_beta import Log


#Create several messages to test with

message01 = [ Message("CAR12345", "mls", "clc", 100, "SUR:HC"), Message("CAR12345", "brk", "mls", 100, "HC1: NOT SLOWING DOWN") , Message("CAR12345", "clc", "mls", 100, "HC3: TEMP 50F HUMIDITY 6%") , Message("CAR12345", "brk", "lis", 100, "SUR: BRK LT ON") , Message("CAR12345", "ccs", "dts", 100, "SUR: DR 23%") ]

logging = Log()
#Go through each item of message

for i in message01:
	print(i)
	logging.Parse_Message_To_Collection(i)

print("Success")
