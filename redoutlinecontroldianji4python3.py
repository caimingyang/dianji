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

 
def exec_cmd(a,d,key_val):
    if(key_val==0x45):
        print("Button CH-")
    elif(key_val==0x46):
        print("Button CH")
    elif(key_val==0x47):
        print("Button CH+")
    elif(key_val==0x44):
        print("Button PREV")
    elif(key_val==0x40):
        print("Button NEXT")
    elif(key_val==0x43):
        print("Button PLAY/PAUSE")
    elif(key_val==0x07):
        print("Button VOL-")
    elif(key_val==0x15):
        print("Button VOL+")
    elif(key_val==0x09):
        print("Button EQ")
    elif(key_val==0x16):
        print("Button 0")
    elif(key_val==0x19):
        print("Button 100+")
    elif(key_val==0x0d):
        print("Button 200+")
    elif(key_val==0x0c):
        print("Button 1")
    elif(key_val==0x18):
        print("Button 2")       
        t1 = threading.Thread(target=l.forward,args=(0.003, 512))
        t1.start()
        t2 = threading.Thread(target=r.backward,args=(0.003, 512))
        t2.start()
    elif(key_val==0x5e):
        print("Button 3")
    elif(key_val==0x08):
        print("Button 4")
        r.backward(0.003, 512)
    elif(key_val==0x1c):
        print("Button 5")
    elif(key_val==0x5a):
        print("Button 6")
        l.forward(0.003, 512)
    elif(key_val==0x42):
        print("Button 7")
    elif(key_val==0x52):
        print("Button 8")
        t1 = threading.Thread(target=l.backward,args=(0.003, 512))
        t1.start()
        t2 = threading.Thread(target=r.forward,args=(0.003, 512))
        t2.start()
        
    elif(key_val==0x4a):
        print("Button 9")
 
if __name__ == '__main__':
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	PIN = 16;
	GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
	l =  Dianji()
	l.setup()
	r =  Dianji()
	r.setIn(31,32,33,35)
	r.setup()
	try:
	    while True:
	        if GPIO.input(PIN) == 0:
	            count = 0
	            while GPIO.input(PIN) == 0 and count < 200:
	                count += 1
	                time.sleep(0.00006)
	
	            count = 0
	            while GPIO.input(PIN) == 1 and count < 80:
	                count += 1
	                time.sleep(0.00006)
	
	            idx = 0
	            cnt = 0
	            data = [0,0,0,0]
	            for i in range(0,32):
	                count = 0
	                while GPIO.input(PIN) == 0 and count < 15:
	                    count += 1
	                    time.sleep(0.00006)
	
	                count = 0
	                while GPIO.input(PIN) == 1 and count < 40:
	                    count += 1
	                    time.sleep(0.00006)
	
	                if count > 8:
	                    data[idx] |= 1<<cnt
	                if cnt == 7:
	                    cnt = 0
	                    idx += 1
	                else:
	                    cnt += 1
	            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:
	                 print("Get the key: 0x%02x" %data[2])
	                 exec_cmd(l,r,data[2])
	except KeyboardInterrupt:
	    GPIO.cleanup();
