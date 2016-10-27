#Author: Abu Chowdhury
#Class: 440W
#Group: BrakingSystem

import json

class brakingsystem:

    def brakestatus(bluetooth):

        with open ('Data') as json_data: #opens json file

            que = json_data.read() #jason read the data

            message = json.loads(que) #message gets upload

            for id in message['CID']:

                message.insert["OID:BSS, DID:LMS, PLD:brakes applied"] #message applied then brake
