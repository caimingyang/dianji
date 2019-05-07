#!/usr/bin/env python
#########################################################
#	File name: stepMotor.py
#	   Author: Jason Dai
#	     Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
 
IN1 = 31
IN2 = 32
IN3 = 33
IN4 = 35
 
def setStep(w1, w2, w3, w4):
	GPIO.output(IN1, w1)
	GPIO.output(IN2, w2)
	GPIO.output(IN3, w3)
	GPIO.output(IN4, w4)
 
def stop():
	setStep(0, 0, 0, 0)
 
def forward(delay, steps):  
	for i in range(0, steps):
		setStep(1, 0, 0, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 0)
		time.sleep(delay)
		setStep(0, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 0, 0, 1)
		time.sleep(delay)
 
def backward(delay, steps):  
	for i in range(0, steps):
		setStep(0, 0, 0, 1)
		time.sleep(delay)
		setStep(0, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 0)
		time.sleep(delay)
		setStep(1, 0, 0, 0)
		time.sleep(delay)
 
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(IN1, GPIO.OUT)
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)
 
def loop():
	while True:
		print "backward..."
		backward(0.003, 512)
		
		print "stop..."
		stop()
		time.sleep(3)
		
		print "forward..."
		forward(0.005, 512)
		
		print "stop..."
		stop()
		time.sleep(3)
 
def destroy():
	GPIO.cleanup()
 
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
