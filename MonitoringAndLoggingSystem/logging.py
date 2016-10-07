
# logging.py
# author: IST411 Group 2
# 9/8/2016
import json
from pymongo import MongoClient

class Log:
	
	def __init__(self):
		#initialize db connection
        def get_db():
		from pymongo import MongoClient
    		client = MongoClient('localhost:27017')
    		db = client.logging
    		return db
	def add_log(db):
    		db.log.insert({"ID" : "Car123","CID":"bks"})

	def get_log(db):
    		return db.log.find_one()

	def JSON_To_Python(self, recieved_messaage):
		return json.loads(recieved_message)		

	def displayLog(self):
		#print out all log message entries
        	db = get_db() 
    		add_log(db)
    		print get_log(db)
		
	#This method add message to log in a database for future use
	def AddMessages():
		pass

	#This method retrievs the message by subsystems
        def RetrieveBySubSystem():
                pass

	#This method retrieves the messages by error from log
        def RetrieveErrors():
                pass

	#This method retrieves all the messages from log
        def RetrieveAll():
                pass
	
	#This method will clear all messages
        def ClearAll():
                pass

	#This method will clear messages up to the date provided
	def ClearupToDate():
		pass
