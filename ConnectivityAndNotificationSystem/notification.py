import json
import smtplib
import hashlib

class Notification :
    def connectivitystatus(bluetooth):
        with open ('Data') as json_data: #opens json file
            que = json_data.read()
            message = json.loads(que)
            for id in message['CID']:
                if id['PLD'] == 'connected':
                    print ('Bluetooth device is now '+id['PLD'])
                    bluetooth = 'True'
        return bluetooth

    def batterypackStatus(kwhStatus):
        with open('Data') as json_data: #opens json file
            que = json_data.read()
            message = json.loads(que)
            for id in message['CID']:
                if id['PLD'] == 'batteryLow':
                    print ('Battery status: ' + id['PLD'])
                    kwhStatus = 'True'
        return kwhStatus


    def doorLock(asd):
        with open('Data') as json_data:  # opens json file
            que = json_data.read()
            message = json.loads(que)
            for id in message['CID']:
                if id['PLD'] == 'locked':
                    print('Door is now: ' + id['PLD'])
                    asd = 'True'

Notification.doorLock(True)
Notification.batterypackStatus(True)
Notification.connectivitystatus(True)
    #md5_object =hashlib.md5()#(md5_object (message).hexdigest())




