import json
import smtplib
import hashlib

class Notification :
    def connectivitystatus(bluetooth=):
        with open ('data') as json_data: #opens json file
            que = json_data.read()
            message = json.loads(que)
            for id in message['CID'] :
                if id['PLD'] == 'connected':
                    print ('Bluetooth device is now '+id['PLD'])
                    bluetooth = 'True'

        return bluetooth
Notification.connectivitystatus(True)


    def batterypackStatus(kwhStatus):
        with open('data') as json_data: #opens json file
            que = json_data.read()
            message = json.loads(que)
            for id['PLD'] == '

    #md5_object =hashlib.md5()#(md5_object (message).hexdigest())




