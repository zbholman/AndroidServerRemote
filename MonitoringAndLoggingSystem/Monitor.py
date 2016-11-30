# monitoring.py
# author: IST411 Group 2
# Version 3
#This class is in charge of monitoring the communications between modules in
#the automobile and checking them for health or other patterns. This module
#also has the capability to intermittedly request status updates from other
#modules and to send alerts if something isn't working correctly

import json
import datetime
from Message import Message
from logging import Log
import threading
import time
import queue

subsys_ids = {'brs':'Braking System','clc':'Climate Control System', 'ems':'Energy Management System', 'ccs':'Command and Control System', 'mls':'Monitoring and Logging System', 'cns':'Connectivity and Notification System', 'dts':'Drivetrain System', 'lts':'Lighting System', 'sac':'Safety and Access Control System'}

class Monitor:
    
	#stores last time subsystems sent out message to comm. bus
    subsys_last_heard = {'brs':0,'clc':0, 'ems':0, 'ccs':0, 'cns':0, 'dts':0, 'lts':0, 'sac':0}

    #stores last known health code of subsystem
	subsys_last_hc = {'brs':3,'clc':3, 'ems':3, 'ccs':3, 'cns':3, 'dts':3, 'lts':3, 'sac':3}
	
    #time in milliseconds for watchdog to ask for subsystem status
    timeout_warning = 5000
    
    #time in milliseconds for watchdog to declare subsystem unresponsive
    timeout_critical = 10000
	
	#time that monitoring was started
	start_monitor_time = 0


    #This method initializes Monitor instance, setting the "last_heard" 
    #times for each subsystem to the time when the monitor was started
    def __init__(self):
        self.start_monitor_time = datetime.datetime.now()
        for subsys in subsys_ids:
            self.subsys_last_heard[subsys] = self.start_monitor_time
	
	#This method should be called by the message threading queue in order
	#to process the message, update watchdogs, interface with CNS and Logger
    def ProcessMessage(self, recieved_message):
		Log.Parse_Message_To_Collection(recieved_message)
		SetLastHeardFrom(recieved_message.Return_Origin_ID())
		if(recieved_message.Return_Payload()[:2:] == "HC"):
			#Do something to pass message to cns 

    #This method sends a ping to the destination subsystem as a status
	#request to see that the subsystem is still functioning and healthy
	#To implement, create a new message object and populate it with the
	#correct data (universal code needed for status update request)
    def PingSystem(self, destination_id):
        toSend = Message('car123', 'mls', 'destination_id', '100', 'Status Update')
    
    #This method sets the last time the subsystem in question broadcasted 
	#a message. This is vital to reset this time for the watchdog to work
    def SetLastHeardFrom(self, origin_id):
        self.subsys_last_heard[origin_id] = datetime.datetime.now()
        
    #This method returns the last time the subsystem in question broadcaste a message. 
    def GetLastHeardFrom(self, subsystem_id):
        return self.subsys_last_heard[subsystem_id]
    
    #This method compares the last time each subsystem has communicated
	#with the current system time. If the difference is greater than a
	#set time limit, the method calls PingSystem(subsystem_id) in an 
	#attempt to see if everything is still functioning properly. If even
	#more time passes, this method calls ThrowUnresponsiveError()
    def CheckWatchdog(self):
        pass
    
    #This method sends out an error message to warn the driver that a 
	#subsystem is unresponsive if it hasn't sent a status update over 
	#a set period of time
    def ThrowUnresponsiveError(self, subsystem_id):
        pass


mon = Monitor()
