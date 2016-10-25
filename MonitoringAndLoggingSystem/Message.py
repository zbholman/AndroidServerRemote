import time
import json

'''
Author: Ivan Iakimenko
Ver: 6
Description: This class stores all of the properties of a message and has methods to convert it to a json string, generate a checksum
based on the payload, and check the generated payload against the one supplied at initialization. If no checksum is available
at initialization, a checksum is automatically generated based on the current payload (this is useful for sending messages so 
you don't have to compute the payload from whatever code you're sending it from)
'''
class Message:
    def __init__(self, car_id, origin_id, destination_id, time_to_live, payload, timestamp=0.0, uuid='0', checksum='0'):
        self.car_id = car_id
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.ttl = time_to_live
        self.payload = payload

        if checksum=='0':
            self.checksum = self.CalculateChecksum()
        else:
            self.checksum = checksum

        if uuid=='0':
            self.uuid = self.GenerateUUID()
        else:
            self.uuid = uuid

        if timestamp == 0.0:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

    #Returns string JSON representation of current message object based on message formatting standard
    def ConvertToJSON(self):
        contents={'CID':self.car_id,'OID':self.origin_id,'DID':self.destination_id, 'TS':self.timestamp, 'TTL':self.ttl, 'UID':self.uuid, 'CKS':self.checksum }
        contents['PLD']=self.payload
        return json.dumps(contents)

    #Returns a dictionary from the message object
    def ConvertToDictionary(self):
        return {"CID": self.car_id, "OID": self.origin_id, "DID": self.destination_id, "TTL": self.ttl, "TS": self.timestamp, "UID": self.uuid, "PLD": self.payload, "CKS": self.checksum}


    #Returns a md5 checksum based on current payload
    def CalculateChecksum(self):
        import hashlib
        return hashlib.md5(self.payload.encode()).hexdigest()

    #Returns a boolean based on whether supplied checksum matches self generated value
    def CompareChecksum(self):
        return self.checksum == self.CalculateChecksum()

    #Returns a random UUID hex value
    def GenerateUUID(self):
        import uuid
        return uuid.uuid4().hex

    #Return the timestamp in a readable format
    def TranslateTimestamp(self):
        return time.ctime(self.timestamp)

'''
This method takes a json string, converts it into a python dictionary object and the returns it as a Message object
This is how you go from a message your subsystem gets on the serial port to a usable message object with variables
The Key in contents['Key'] must match the standard abbreviations for message properties
'''
def ConvertFromJSON(json_string):
    contents = json.loads(json_string)
    return Message(contents['CID'], contents['OID'], contents['DID'], contents['TTL'], contents['PLD'], contents['TS'], contents['UID'], contents['CKS'])    
