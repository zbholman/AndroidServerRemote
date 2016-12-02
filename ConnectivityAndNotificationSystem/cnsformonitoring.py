import json, smtplib
import Message

class CNS:
	def receivemessage(receivedmessage) :
		mail = smtplib.SMTP('smtp.gmail.com',587)#gmail uses 587
		mail.ehlo()
		mail.starttls#encrypts
		mail.login('abc@gmail.com','password')#email address, pasword
		Content = receivedmessage(receivedmessage)
		
		mail.sendmail('fromemail','receiver',Content)#sender,recepient,content

	def receivedmessage(info) :
		contentpayload = info.Return_Payload()
		contentorigin = info.Return_Origin_ID()
		if contentorigin == 'ems' :
			#if contentpayload == 'HC1':#open file object and check for Emmergency in PLd string
			#I think this is what you want and you won't need the second if statement here.
			content = contentpayload.rpartition(':')[2]
				#content = "Battery is running low"
		return content

	'''	for id in message['OID'] == "brk" :
			elif id['PLD'] == 'automatedBrakesfailed':#open file object and check for Emmergency in PLd string
			content = ("The automated brakes are not working")

		for id in message['OID'] == "lis" :
			elif id['PLD'] == 'frontleftlightfailed':#open file object and check for Emmergency in PLd string
			content = ("The Front left light is not working")

			elif id['PLD'] == 'frontlefrightfailed':#open file object and check for Emmergency in PLd string
			content = ("The Front Right light is not working")

			elif id['PLD'] == 'rearleftlightfailed':#open file object and check for Emmergency in PLd string
			content = ("The Rear Left light is not working")

			elif id['PLD'] == 'rearrightlightfailed':#open file object and check for Emmergency in PLd string
			content = ("The Rear Right light is not working")

		for id in message['OID'] == "lis" :
			elif id['PLD'] == 'automatedBrakesfailed':#open file object and check for Emmergency in PLd string
			content = ("The automated brakes are not working")

		return content
	def receivedhealthcode (content1)
	''' def ConvertToDictionary(self):
        return {"CID": self.car_id, "OID": self.origin_id, "DID": self.destination_id, "TTL": self.ttl, "TS": self.timestamp, "UID": self.uuid, "PLD": self.payload, "CKS": self.checksum}


    #Returns the payload of the message
    def Return_Payload(self):
        return self.payload

    #Returns the origin ID of the message
    def Return_Origin_ID(self):
        return self.origin_id

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
