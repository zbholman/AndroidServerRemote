# Enter notification classes here 
# define notification classes
import json
import hashlib

class Connected_notification:
	def ConvertFromJSON(json_string):
    	contents = json.loads(json_string)
    	return Message(contents['CID'], contents['OID'], contents['DID'], contents['HC'], contents['TS'], contents['TTL'], contents['PLD'], contents['UID'], contents['CKS'])
	
	def cell_connection (self,Cellular):
		devicename=''
		if (self.Cellular == True):
			print('The %s is now connected to the cellular network' % devicename)
		else:
			print ('No Cellular device is connected at the moment')
		return devicename
	def blue_connection (self,Bluetooth):
		devicename_phone=''
		if(self.Bluetooth == True):
			print('This %s is now connected via Bluetooth ' % devicename_phone )
		else:
			print ('No device connected. \n Please turn on bluetooth on your device.')
		return devicename_phone
	def tms_notification(self,USB):
		device=''
		if (self.USB == True):
			print('The %s is now connected through USB' % device)
		else:
			print ('No device is connected through USB')
		return device
	def BatteryPackStatus(self,kwhLevel):
		if self.kwhLevel <= LITHIUMKWHPACKLOW:
			NOTIFYLEVEL = 'CRITICAL'
			print (NOTIFYLEVEL)
		elif self.kwhLevel <= LITHIUMKWHPACKMEDIUM:
			NOTIFYLEVEL = 'HIGH'
			print(NOTIFYLEVEL)
		elif self.kwhLevel <= LITHIUMKWHPACKHIGH:
			NOTIFYLEVEL = 'MEDIUM'
			print(NOTIFYLEVEL)
		elif self.kwhLevel <= LITHIUMKWHPACKFULL:
			NOTIFYLEVEL = 'LOW'
			print(NOTIFYLEVEL)
