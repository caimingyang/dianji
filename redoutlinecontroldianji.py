<<<<<<< HEAD
=======
Last login: Thu Apr  4 20:47:34 on console
caimingyangdeMacBook-Pro:~ caimingyang$ history|grep ssh
  188  ssh root@172.27.129.250
  194  ssh root@172.27.129.250
  377  ssh 192.168.0.105
  378  ssh 192.168.0.105
  379  ssh 192.168.0.105
  380  ssh pi@192.168.0.105
  381  history|grep ssh
  382  ssh 192.168.0.105
  383  ssh pi@192.168.0.105
  384  ssh pi@192.168.0.105
  385  ssh pi@192.168.0.105
  386  ssh pi@192.168.0.105
  387  ssh pi@192.168.0.105
  388  ssh pi@192.168.0.105
  389  ssh pi@192.168.0.105
  391  ssh pi@192.168.0.105
  394  ssh pi@192.168.0.105
  395  ssh pi@192.168.0.105
  396  ssh pi@192.168.0.105
  397  ssh pi@192.168.0.105
  398  ssh pi@192.168.0.105
  400  ssh pi@192.168.0.105
  401  ssh pi@192.168.0.105
  411  ssh pi@192.168.0.105
  412  ssh pi@192.168.0.105
  413  ssh pi@192.168.0.105
  414  ssh pi@192.168.0.105
  419  ssh pi@192.168.0.105
  421  ssh pi@192.168.0.105
  423  ssh pi@192.168.0.105
  424  ssh pi@192.168.0.105
  445  history|grep ssh
  446  ssh pi@192.168.0.105
  462  history |grep ssh
  463  ssh pi@192.168.0.105
  464  ssh pi@192.168.0.105
  465  ssh pi@192.168.0.105
  466  ssh pi@192.168.0.105
  467  ssh pi@192.168.0.105
  468  ssh pi@192.168.0.105
  469  ssh pi@192.168.0.105
  478  history|grep ssh
  479  ssh pi@192.168.0.105
  480  ssh pi@192.168.0.105
  481  ssh pi@192.168.0.105
  482  ssh pi@192.168.0.105
  501  history|grep ssh
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ ssh pi@192.168.0.105
pi@192.168.0.105's password: 
Linux raspberrypi 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Mar 30 14:48:35 2019

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ 
pi@raspberrypi:~ $ ls
a.txt        Desktop    Downloads  nano.save  Public        Templates
caimingyang  Documents  Music      Pictures   python_games  Videos
pi@raspberrypi:~ $ pw
-bash: pw: command not found
pi@raspberrypi:~ $ pwd
/home/pi
pi@raspberrypi:~ $ ls
a.txt        Desktop    Downloads  nano.save  Public        Templates
caimingyang  Documents  Music      Pictures   python_games  Videos
pi@raspberrypi:~ $ cd caimingyang
pi@raspberrypi:~/caimingyang $ ls
dianji  MFRC522-python  python      shuzhi  test       test.py
lcd     pi-rc522        redoutline  SPI-Py  test22.py
pi@raspberrypi:~/caimingyang $ cd dianji
pi@raspberrypi:~/caimingyang/dianji $ ls
dianji2.py     dianji.py        dianjiright.py              testClass.py
dianjileft.py  dianjiright2.py  redoutlinecontroldianji.py  testClassRight.py
pi@raspberrypi:~/caimingyang/dianji $ more redoutlinecontroldianji.py
#!/usr/bin/env python
#########################################################
#	File name: stepMotor.py
#	   Author: Jason Dai
#	     Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

	IN1 = 11
	IN2 = 12
	IN3 = 13
	IN4 = 15

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
	 
	def setup(self):

		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)
 
	def loop(self):
		while True:
			print "backward..."
			self.backward(0.003, 512)
			
			print "stop..."
			self.stop()
			time.sleep(3)
			
			print "forward..."
			self.forward(0.005, 512)
			
			print "stop..."
			self.stop()
			time.sleep(3)
 
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
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ python redoutlinecontroldianji.py
^Cpi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ ls
dianji2.py     dianji.py        dianjiright.py              testClass.py
dianjileft.py  dianjiright2.py  redoutlinecontroldianji.py  testClassRight.py
pi@raspberrypi:~/caimingyang/dianji $ python dianjiright.py
backward...
stop...
forward...
^C^Z
[1]+  Stopped                 python dianjiright.py
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ python dianjileft.py
backward...
stop...
forward...
stop...
backward...
stop...
forward...
stop...
backward...
stop...
forward...
stop...
backward...
stop...
forward...
^Z
[2]+  Stopped                 python dianjileft.py
pi@raspberrypi:~/caimingyang/dianji $ ^C
pi@raspberrypi:~/caimingyang/dianji $ ls
dianji2.py     dianji.py        dianjiright.py              testClass.py
dianjileft.py  dianjiright2.py  redoutlinecontroldianji.py  testClassRight.py
pi@raspberrypi:~/caimingyang/dianji $ python dianji2.py
backward...
backward...
backward...
backward...
backward...
backward...
^Z
[3]+  Stopped                 python dianji2.py
pi@raspberrypi:~/caimingyang/dianji $ ^C
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ more dianji2.p
more: stat of dianji2.p failed: No such file or directory
pi@raspberrypi:~/caimingyang/dianji $ more dianji2.py
#!/usr/bin/env python
#########################################################
#	File name: stepMotor.py
#	   Author: Jason Dai
#	     Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
 
IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
 
def setStep(w1, w2, w3, w4):
	GPIO.output(IN1, w1)
	GPIO.output(IN2, w2)
	GPIO.output(IN3, w3)
	GPIO.output(IN4, w4)
 
def stop():
	setStep(0, 0, 0, 0)
 
--More--(34%)Connection to 192.168.0.105 closed by remote host.
Connection to 192.168.0.105 closed.
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ ssh pi@192.168.0.105
pi@192.168.0.105's password: 
Linux raspberrypi 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Apr  4 13:32:18 2019

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberrypi:~ $ ls
a.txt        Desktop    Downloads  nano.save  Public        Templates
caimingyang  Documents  Music      Pictures   python_games  Videos
pi@raspberrypi:~ $ cd caimingyang/
pi@raspberrypi:~/caimingyang $ ls
dianji  MFRC522-python  python      shuzhi  test       test.py
lcd     pi-rc522        redoutline  SPI-Py  test22.py
pi@raspberrypi:~/caimingyang $ cd dianji
pi@raspberrypi:~/caimingyang/dianji $ ls
dianji2.py     dianji.py        dianjiright.py              testClass.py
dianjileft.py  dianjiright2.py  redoutlinecontroldianji.py  testClassRight.py
pi@raspberrypi:~/caimingyang/dianji $ python redoutlinecontroldianji.py
Get the key: 0x18
Button 2
Get the key: 0x08
Button 4
Get the key: 0x5a
Button 6
Get the key: 0x52
Button 8
Get the key: 0x52
Button 8
Get the key: 0x18
Button 2
Get the key: 0x18
Button 2
Get the key: 0x52
Button 8
Get the key: 0x52
Button 8
Get the key: 0x5a
Button 6
Get the key: 0x08
Button 4
^Z
[1]+  Stopped                 python redoutlinecontroldianji.py
pi@raspberrypi:~/caimingyang/dianji $ ^C
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ more redoutlinecontroldianji.py
>>>>>>> e60d9178bbcbb61aa567a411a4d19a70070e32a5
#!/usr/bin/env python
#########################################################
#	File name: stepMotor.py
#	   Author: Jason Dai
#	     Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

	IN1 = 11
	IN2 = 12
	IN3 = 13
	IN4 = 15

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
	 
	def setup(self):

		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)
 
	def loop(self):
		while True:
			print "backward..."
			self.backward(0.003, 512)
			
			print "stop..."
			self.stop()
			time.sleep(3)
			
			print "forward..."
			self.forward(0.005, 512)
			
			print "stop..."
			self.stop()
			time.sleep(3)
 
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
<<<<<<< HEAD
=======
pi@raspberrypi:~/caimingyang/dianji $  
pi@raspberrypi:~/caimingyang/dianji $ 
pi@raspberrypi:~/caimingyang/dianji $ pwd
/home/pi/caimingyang/dianji
pi@raspberrypi:~/caimingyang/dianji $ exit
logout
There are stopped jobs.
pi@raspberrypi:~/caimingyang/dianji $ exit
logout
Connection to 192.168.0.105 closed.
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ pwd
/Users/caimingyang
caimingyangdeMacBook-Pro:~ caimingyang$ sftp pi@192.168.0.105
pi@192.168.0.105's password: 
Connected to pi@192.168.0.105.
sftp> ls
Desktop         Documents       Downloads       Music           Pictures        
Public          Templates       Videos          a.txt           caimingyang     
nano.save       python_games    
sftp> cd caimingyang
sftp> ls
MFRC522-python  SPI-Py          dianji          lcd             pi-rc522        
python          redoutline      shuzhi          test            test.py         
test22.py       
sftp> cd dianji
sftp> ls
dianji.py                               dianji2.py                              
dianjileft.py                           dianjiright.py                          
dianjiright2.py                         redoutlinecontroldianji.py              
testClass.py                            testClassRight.py                       
sftp> get redoutlinecontroldianji.py
Fetching /home/pi/caimingyang/dianji/redoutlinecontroldianji.py to redoutlinecontroldianji.py
/home/pi/caimingyang/dianji/redoutlinecontrol 100% 4501   556.9KB/s   00:00    
sftp> exit
caimingyangdeMacBook-Pro:~ caimingyang$ ls
Applications			aaa
Applications (Parallels)	default.conf
Desktop				eclipse
Documents			eclipse-workspace
Downloads			knime-workspace
Library				nginx.conf
Movies				python
Music				redoutlinecontroldianji.py
Pictures			requirements.txt
Public				test
VirtualBox VMs			未命名.ipynb
caimingyangdeMacBook-Pro:~ caimingyang$ history|grep git
  284  git clone https://github.com/ICT-BDA/EasyML
  285  git clone https://github.com/ICT-BDA/EasyML
  286  git clone https://github.com/ICT-BDA/EasyML
  295  git clone https://github.com/caimingyang/python.git
  311  git clone https://github.com/caimingyang/redoutline.git
  321  git clone https://github.com/caimingyang/redoutline.git
  344  git clone https://github.com/caimingyang/temperature.git
  375  history|grep git
  393  history|grep git
  444  history|grep git
  507  history|grep git
caimingyangdeMacBook-Pro:~ caimingyang$ ls
Applications			aaa
Applications (Parallels)	default.conf
Desktop				eclipse
Documents			eclipse-workspace
Downloads			knime-workspace
Library				nginx.conf
Movies				python
Music				redoutlinecontroldianji.py
Pictures			requirements.txt
Public				test
VirtualBox VMs			未命名.ipynb
caimingyangdeMacBook-Pro:~ caimingyang$ more redoutlinecontroldianji.py
#!/usr/bin/env python
#########################################################
#       File name: stepMotor.py
#          Author: Jason Dai
#            Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

        def setIn(self,w1, w2, w3, w4):
                self.IN1=w1
                self.IN2=w2
                self.IN3=w3
                self.IN4=w4
         
:...skipping...
#!/usr/bin/env python
#########################################################
#       File name: stepMotor.py
#          Author: Jason Dai
#            Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

        def setIn(self,w1, w2, w3, w4):
                self.IN1=w1
                self.IN2=w2
                self.IN3=w3
                self.IN4=w4
         
        def setStep(self,w1, w2, w3, w4):
:...skipping...
#!/usr/bin/env python
#########################################################
#       File name: stepMotor.py
#          Author: Jason Dai
#            Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

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
         
        def setup(self):

                GPIO.setup(self.IN1, GPIO.OUT)
                GPIO.setup(self.IN2, GPIO.OUT)
                GPIO.setup(self.IN3, GPIO.OUT)
                GPIO.setup(self.IN4, GPIO.OUT)
 
        def loop(self):
                while True:
                        print "backward..."
                        self.backward(0.003, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
                        
                        print "forward..."
                        self.forward(0.005, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
 
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
caimingyangdeMacBook-Pro:~ caimingyang$ more redoutlinecontroldianji.py
#!/usr/bin/env python
#########################################################
#       File name: stepMotor.py
#          Author: Jason Dai
#            Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

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
         
        def setup(self):

                GPIO.setup(self.IN1, GPIO.OUT)
                GPIO.setup(self.IN2, GPIO.OUT)
                GPIO.setup(self.IN3, GPIO.OUT)
                GPIO.setup(self.IN4, GPIO.OUT)
 
        def loop(self):
                while True:
                        print "backward..."
                        self.backward(0.003, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
                        
                        print "forward..."
                        self.forward(0.005, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
 
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
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ 
caimingyangdeMacBook-Pro:~ caimingyang$ more redoutlinecontroldianji.py
#!/usr/bin/env python
#########################################################
#       File name: stepMotor.py
#          Author: Jason Dai
#            Date: 2015/01/26
#########################################################
import RPi.GPIO as GPIO
import time
import threading

class Dianji:       

        IN1 = 11
        IN2 = 12
        IN3 = 13
        IN4 = 15

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
         
        def setup(self):

                GPIO.setup(self.IN1, GPIO.OUT)
                GPIO.setup(self.IN2, GPIO.OUT)
                GPIO.setup(self.IN3, GPIO.OUT)
                GPIO.setup(self.IN4, GPIO.OUT)
 
        def loop(self):
                while True:
                        print "backward..."
                        self.backward(0.003, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
                        
                        print "forward..."
                        self.forward(0.005, 512)
                        
                        print "stop..."
                        self.stop()
                        time.sleep(3)
 
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
>>>>>>> e60d9178bbcbb61aa567a411a4d19a70070e32a5
