
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
                db = client.dbNiravkumar
                return db

        def add_message(db):
                db.logging.insert({"PLD": "payload: This message format defined by subteams", "UID": "cc077cc47be14d968fc1947e7edd3436", "CKS": "8fcffdcd1c1dbd62c199aa2a13c9043a", "CID": "car10393", "DID": "ML", "HC": 3, "TTL": 100, "OID": "CC", "TS": 1476407469.717848})

        def get_message(db):
                return db.logging.find_one()

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
