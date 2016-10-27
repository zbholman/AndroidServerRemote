
# logging.py
# author: IST411 Group 2
# 9/8/2016
# Version 4
#This class is the code responsible for creating logs and storing them in a Mongo Database. 
import json
from pymongo import MongoClient

class Log:
	def __init__(self):
		#initialize db connection
	def get_db():
                from pymongo import MongoClient
                client = MongoClient('localhost:27017')
                db = client.dbNiravkumar
                return db
	
	#Method that determines what collections to put the message into
	#and puts that message into the collection.
	#Sorts it by HealthCode, Origin, and puts all messages into a default collection
	def Parse_Message_To_Collection(inc_message):
		
		#If the payload contains a healthcode, put it in the errors collection
        	if(inc_message.Return_Payload()[:2:] == "HC"):
                	add_message(inc_message, db.errors)

		#Put the message into the collection dependant on where the message originated from
        	if(inc_message.Return_Origin_ID() == "brs"):
                	add_message(inc_message, db.brs)                                                              
        	elif(inc_message.Return_Origin_ID() == "clc"):
                	add_message(inc_message, db.clc)
       		elif(inc_message.Return_Origin_ID() == "ems"):
                	add_message(inc_message, db.ems)
        	elif(inc_message.Return_Origin_ID() == "ccs"):
                	add_message(inc_message, db.ccs) 
        	elif(inc_message.Return_Origin_ID() == "mls"):
                	add_message(inc_message, db.mls)
        	elif(inc_message.Return_Origin_ID() == "cns"):
                	add_message(inc_message, db.cns)
        	elif(inc_message.Return_Origin_ID() == "dts"):
                	add_message(inc_message, db.dts)
        	elif(inc_message.Return_Origin_ID() == "lis"):
                	add_message(inc_message, db.lis)
        	elif(inc_message.Return_Origin_ID() == "sac"):
                	add_message(inc_message, db.sac)
		
		#Put all of the messages into one central default collection
		add_message(inc_message)


	#Method to add a message to the mongo database
        def add_message(message, collection):
		collection.insert(message.Convert_To_Dictionary())
	

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
