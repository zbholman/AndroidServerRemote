#Joey Lee
#Version 1.00
#10-2-16

import nfc
import subprocess

#If a tag is connected:Print out tag info
def connected(tag):
    subprocess.Popen("/usr/bin/python /home/pi/PSUABFA16IST440/SafetyAndAccessControlSystem/Doors_unlock.py", shell=True)
    print(tag)

def verify(tag):
    tag.dump()
    print('False')
    return False


#Locates and Opens contactless reader on raspberry Pi Uart
clf = nfc.ContactlessFrontend('tty:AMA0:pn532')

print(clf)

#Starts a class method if a tag is recognized
while True :
    clf.connect(rdwr={'on-connect': connected})
    break

clf.close()
