import json

class brakingsystem:

    def brakestatus(bluetooth):

        with open ('Data') as json_data: #opens json file

            que = json_data.read()

            message = json.loads(que)

            for id in message['CID']:

                message.insert["OID:BSS, DID:LMS, PLD:brakes applied"]
