import serial
from threading import Thread
import queue

ser = serial.Serial('/dev/ttyUSB0', 9500) #Sets up a serialization port.
testString = "Hello!"
print ('Sending "%s"' % testString)
ser.write('%s\n' % testString)

while True:
        incomingMsg = ser.readline().strip()
        print('Recieved %s' % incomingMsg)
        ser.write ('RPI Recieved: %s\n' % incomingMsg)


#Tells the queue that processing the task is complete

def taskt(t):
        while True:
                print(t.get())
                t.task_done()
#setup the quese object as t 0 = infinite
#sets the number of threads obkects to be 10
t = queue.Queue(maxsize=0)
num_threads = 10

#Loop to put 100 numbers on the queue
for y in range(100):
        t.put(x)

#looping 10 threads
#create worker thread
#worker is ended when the main thread ends

