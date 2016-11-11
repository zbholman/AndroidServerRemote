
# logging.py
# author: IST411 Group 2
# 9/8/2016
# Version 4
#This class is the code responsible for creating logs and storing them in a Mongo Database. 
import json
from pymongo import MongoClient
from Message import Message

class Log:

	client = MongoClient()
	global db 
	db = client.dbCar


	def __init__(self):
		#initialize db connection
		client = MongoClient()
		db = client.dbCar

	
	#Method that determines what collections to put the message into
	#and puts that message into the collection.
	#Sorts it by HealthCode, Origin, and puts all messages into a default collection
	def Parse_Message_To_Collection(self, inc_message):
		print(inc_message)
		#If the payload contains a healthcode, put it in the errors collection
		if(inc_message.Return_Payload()[:2:] == "HC"):
               		 self.add_message(inc_message, db.errors)
		#Put the message into the collection dependant on where the message originated from
        	
		self.add_message(inc_message , getattr(db, inc_message.Return_Origin_ID() ) )
		
		#Put all of the messages into one central default collection
		self.add_message(inc_message)
	

	#Method to add a message to the mongo database
        def add_message(self, message, c = db.default):
		c.insert(message.ConvertToDictionary())	


	
	#drop all tables. This is for testing purposes. This method MUST be removed before build
	def bobby_drop_tables(self):
		for i in db.collection_names(): #go through all of the collections in the database
			if( not( i == "system.indexes")): #Ensuring that the system.indexes collection does not get deleted		
				getattr(db, i).drop() #This line is doing 'db.[value at i].drop()						

	

	#returns a message from the current database, collection 'logging'
        def get_message(db):
                return db.logging.find_one()
	#inits class for testing purposes
        if __name__ == "__main__":

                db = get_db()
                add_message(db)
                print get_message(db)



	#This method add message to log in a database for future use
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
