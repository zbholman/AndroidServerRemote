#Joey Lee
#Version 1.00
#10-2-16

import nfc

#If a tag is connected:Print out tag info
def connected(tag): print(tag); return False

#Locates and Opens contactless reader on raspberry Pi Uart
clf = nfc.ContactlessFrontend('ttys0')

print(clf)

#Should Print Out a Certain String
assert(clf == 'Adafruit Board on ttys0:USB0:pn532' )

#Tests if a tag is recognized and removed
clf.connect(rdwr={})

#Starts a class method if a tag is recognized
clf.connect(rdwr={'on-connect': connected})
