
# logging.py
# author: IST411 Group 2
# 9/8/2016
import json




class Log:

	def __init__(self):
		#initialize db connection


	def JSON_To_Python(self, recieved_messaage):
		return json.loads(recieved_message)		

	def displayLog(self):
		#print out all log message entries
		
	#This method stores the log in a database for future use
	def WriteToDB(self):
		pass
