import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

	IN1 = 11
	IN2 = 12
	IN3 = 13
	IN4 = 15
	record = 0
	def setIn(self,w1, w2, w3, w4):
		self.IN1=w1
		self.IN2=w2
		self.IN3=w3
		self.IN4=w4
	 
	def setStep(self,w1, w2, w3, w4):
		GPIO.output(self.IN1, w1)
		GPIO.output(self.IN2, w2)
		GPIO.output(self.IN3, w3)
		GPIO.output(self.IN4, w4)
	
	def stop(self):
		self.setStep(0, 0, 0, 0)
	 
	def forward(self,delay, steps):  
		for i in range(0, steps):
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)
			self.record =self.record + 1
	 
	def backward(self,delay, steps):  
		for i in range(0, steps):
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)
			self.record =self.record - 1
	 
	def setup(self):

		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)
		
	def getRecord(self):

		return self.record


	def reset(self):
		if self.record>0:
			self.backward(0.005,self.record)
		if self.record<0:
			self.forward(0.005,abs(self.record))


	def loop(self):
		while True:
			self.backward(0.03, 512)
			
			print ("stop...")
			self.stop()
			time.sleep(3)
			
			print ("forward...")
			self.forward(0.03, 512)
			
			print ("stop...")
			self.stop()
			time.sleep(3)
