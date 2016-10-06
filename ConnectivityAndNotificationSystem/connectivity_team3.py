import bluetooth
import socket
import threading
import queue
import bluetooth
import time

# Connects us to a pi
class ConnectToPi :
        def __init__(self):
                s = socket.socket()
                host = socket.gethostname()
                port = 12345
                s.connect((host,port))
                print s.recv(1024)
                s.close()


# Listens for a connection from a pi
class ConnectFromPi:
        def __init__(self):
                s = socket.socket()
                host = socket.gethostname()
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

# Connection to Pi2 via Pi1
class PiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.200 #IP address for pi 1
                port = 12345
                s.connect((host,port))
                print s.recv(1024)
                s.close()

				class FromPiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.201
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

class ConnectToServer:
        def __init__(self, input_queue, output_queue):
                threading.Thread.__init__(self)
                self.input_queue = input_queue
                self.output_queue = output_queue
                self.HOST = ''
                self.PORT = 8888
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                        self.s.bind((self.HOST, self.PORT))
                except socket.error, msg:
                        print "Binding socket failed, error message: " + msg[1]

        target_name = "My Phone"
        target_address = None

        data_sent = False

        while True:
                nearby_devices = bluetooth.discover_devices()

                for bdaddr in nearby_devices:
                        if target_name == bluetooth.lookup_name( bdaddr ):
                                target_address = bdaddr
                                 break
								 class FromPiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.201
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

class ConnectToServer:

        def __init__(self, input_queue, output_queue):
                threading.Thread.__init__(self)
                self.input_queue = input_queue
                self.output_queue = output_queue
                self.HOST = ''
                self.PORT = 8888
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                        self.s.bind((self.HOST, self.PORT))
                except socket.error, msg:
                        print "Binding socket failed, error message: " + msg[1]

        target_name = "My Phone"
        target_address = None

        data_sent = False

        while True:
                nearby_devices = bluetooth.discover_devices()

                for bdaddr in nearby_devices:
                        if target_name == bluetooth.lookup_name( bdaddr ):
                                target_address = bdaddr
                                 break
class FromPiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.201
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

class ConnectToServer:

        def __init__(self, input_queue, output_queue):
                threading.Thread.__init__(self)
                self.input_queue = input_queue
                self.output_queue = output_queue
                self.HOST = ''
                self.PORT = 8888
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                        self.s.bind((self.HOST, self.PORT))
                except socket.error, msg:
                        print "Binding socket failed, error message: " + msg[1]

        target_name = "My Phone"
        target_address = None

        data_sent = False

        while True:
                nearby_devices = bluetooth.discover_devices()

                for bdaddr in nearby_devices:
                        if target_name == bluetooth.lookup_name( bdaddr ):
                                target_address = bdaddr
                                 break
class FromPiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.201
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

class ConnectToServer:

        def __init__(self, input_queue, output_queue):
                threading.Thread.__init__(self)
                self.input_queue = input_queue
                self.output_queue = output_queue
                self.HOST = ''
                self.PORT = 8888
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                        self.s.bind((self.HOST, self.PORT))
                except socket.error, msg:
                        print "Binding socket failed, error message: " + msg[1]

        target_name = "My Phone"
        target_address = None

        data_sent = False

        while True:
                nearby_devices = bluetooth.discover_devices()

                for bdaddr in nearby_devices:
                        if target_name == bluetooth.lookup_name( bdaddr ):
                                target_address = bdaddr
                                 break

class FromPiToPiConnection:
        def __init__(self):
                s = socket.socket()
                host = 192.168.1.201
                port = 12345
                s.bind((host,port))
                s.listen(5)

                while True:
                        c, addr = s.accept()
                        print 'Got connection from',addr
                        c.send('Thank you for connecting')
                        c.close()

class ConnectToServer:

        def __init__(self, input_queue, output_queue):
                threading.Thread.__init__(self)
                self.input_queue = input_queue
                self.output_queue = output_queue
                self.HOST = ''
                self.PORT = 8888
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                        self.s.bind((self.HOST, self.PORT))
                except socket.error, msg:
                        print "Binding socket failed, error message: " + msg[1]

        target_name = "My Phone"
        target_address = None

        data_sent = False

        while True:
                nearby_devices = bluetooth.discover_devices()

                for bdaddr in nearby_devices:
                        if target_name == bluetooth.lookup_name( bdaddr ):
                                target_address = bdaddr
                                 break
  if (target_address is not None) and (not data_sent):
'''print "found target bluetooth device with address ", target_address
 send_data()'''
                        data_sent = True
                else:
'''print "could not find target bluetooth device nearby"
to mark 'connection dropped''''
                        data_sent = False
                time.sleep(1)

def BACKUP_CONNECTION(self,connection):
#function for a back up connection in the even the first connection fails
