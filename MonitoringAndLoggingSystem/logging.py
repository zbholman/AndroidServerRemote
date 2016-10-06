
# logging.py
# author: IST411 Group 2
# 9/8/2016
import json
from pymongo import MongoClient

class Log:
	
	conn = object
	
	def __init__(self):
			#initialize db connection
        def get_db():
		from pymongo import MongoClient
    		client = MongoClient('localhost:27017')
    		db = client.logging
    		return db
	def add_log(db):
    		db.log.insert({"ID" : "Car123"})

	def get_log(db):
    		return db.log.find_one()

	def JSON_To_Python(self, recieved_messaage):
		return json.loads(recieved_message)		

	def displayLog(self):
		#print out all log message entries
        	db = get_db() 
    		add_log(db)
    		print get_log(db)
		
	#This method stores the log in a database for future use
	def WriteToDB(self):
		pass
