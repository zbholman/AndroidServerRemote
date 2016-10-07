'''python code to open json object and '''
import json#import for json file
import smtplib#import for simple mail transfer protocol

content = 'emergency stuuf here'# content of the email
mail = smtplib.SMTP('smtp.gmail.com',587)#gmail uses 587
mail.ehlo()
mail.starttls#encrypts
mail.login('abc@gmail.com','password')#email address, pasword
mail.sendmail('fromemail','receiver',content)#sender,recepient,content
with open ('file') as json_data :#opens json file
        message = json.load(json_data)#loads file into message
        for id in message['CID'] : #for each car Id
            messages= open(message['PLD'])
            if (messages=='Emergency'):#open file object and check for Emmergency in PLd string
                mail.sendmail('fromemail','receiver',content)#sender,recepient,content

