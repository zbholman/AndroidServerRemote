
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
		client = MongoClient()
		db = client.dbCar

	#NOT SURE WHAT THIS METHOD DOES. PLEASE EXPLAIN TO ME(ION) NIRAVH

	#def get_db():
#                from pymongo import MongoClient
#                client = MongoClient('localhost:27017')
#                db = client.dbNiravkumar
#                return db

	
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


	#Methods to check if the collections exist

	#Check if errors collection exists
	def Check_Collection_errors():
        	exist_flag = False #Flag on if the collection exists. Will be changed to True if the collection does exist
        	for i in db.collection_names(): #Loop through all of the collections on the database
                	if(i == "errors"): #If the current index is the collection we are looking for, set the exist flag to true
                        	exist_flag = True

        	if(not(exist_flag)): #If the flag was never set to true after the loop
                	db.errors.insert_one({"Init": "Initialization of errors collection"}) #Initialize the collection

	#Check if the break system collection exists
	def Check_Collection_brs():
        	exist_flag = False
        	for i in db.collection_names():
                	if(i == "brs"):
                        	exist_flag = True

        	if(not(exist_flag)):
                	db.brs.insert_one({"Init": "Initialization of brs collection"})

	#check if the climate control system collection exists
        def Check_Collection_clc():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "clc"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of clc collection"})

        #check if the energy management system collection exists
        def Check_Collection_ems():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "ems"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of ems collection"})

        #check if the command and control system collection exists
        def Check_Collection_ccs():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "ccs"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of ccs collection"})
      
	  #check if the monitoring and logging system collection exists
        def Check_Collection_mls():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "mls"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of mls collection"})

        #check if the connectivity and notification system collection exists
        def Check_Collection_cns():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "cns"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of cns collection"})

        #check if the drive train system collection exists
        def Check_Collection_dts():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "dts"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of dts collection"})

        #check if the lighting system collection exists
        def Check_Collection_lis():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "lis"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of lis collection"})

        #check if the safety and access system collection exists
        def Check_Collection_sac():
                exist_flag = False
                for i in db.collection_names():
                        if(i == "sac"):
                                exist_flag = True

                if(not(exist_flag)):
                        db.brs.insert_one({"Init": "Initialization of sac collection"})


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
