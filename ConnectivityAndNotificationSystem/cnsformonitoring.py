import json, smtplib

class CNS:
	def receivemessage(Monitoring) :
		mail = smtplib.SMTP('smtp.gmail.com',587)#gmail uses 587
		mail.ehlo()
		mail.starttls#encrypts
		mail.login('abc@gmail.com','password')#email address, pasword
		Content = receivedmessage(Monitoring)
		
		mail.sendmail('fromemail','receiver',Content)#sender,recepient,content

	def receivedmessage(info) :
		with open (info) as json_data :
		monitoringreceive = json_data.read()
		message = json.loads(monitoringreceive)
		for id in message['OID'] == "ems" :
			if id['PLD'] == 'batteryLow':#open file object and check for Emmergency in PLd string
			content = ("Battery is running low")

		for id in message['OID'] == "brk" :
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
		
