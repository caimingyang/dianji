#!/usr/bin/env python
#########################################################
#	File name: stepMotor.py
#	   Author: Jason Dai
#	     Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading
from sdk.Dianji import Dianji
from kafkareceiver import KafkaReceiver
if __name__ == '__main__':
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	c =  Dianji()
	c.setIn(36,37,38,40)
	c.setup()
	k = KafkaReceiver()
	k.setDianji(c)
	k.createThread()
	
	try:
	    while True:
                print ("backward...")
                c.backward(0.03, 128)
                print (c.getRecord())
                print ("stop...")
                c.stop()
                time.sleep(3)
                c.reset()
                print ("forward...")
                c.forward(0.03, 128)
                print (c.getRecord())
                print ("stop...")
                c.stop()
                time.sleep(3)
                c.reset()
	except KeyboardInterrupt:
	    GPIO.cleanup();
