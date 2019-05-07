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
from kafka import KafkaConsumer, TopicPartition


if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    l =  Dianji()
    l.setup()
    r =  Dianji()
    r.setIn(31,32,33,35)
    r.setup()
    consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
    consumer.subscribe('car')
    print('consumer connected')
    try:
        for msg in consumer:
            print(msg)
            res = msg.value.decode()
            print(res)
            if res == 'forward':
                t1 = threading.Thread(target=l.forward,args=(0.003, 512))
                t1.start()
                t2 = threading.Thread(target=r.backward,args=(0.003, 512))
                t2.start()
            elif res == 'backward': 
                t1 = threading.Thread(target=r.forward,args=(0.003, 512))
                t1.start()
                t2 = threading.Thread(target=l.backward,args=(0.003, 512))
                t2.start()
            elif res == 'left':
                t1 = threading.Thread(target=l.forward,args=(0.003, 512))
                t1.start()
                t2 = threading.Thread(target=r.forward,args=(0.003, 512))
                t2.start()
            elif res == 'right':
                t1 = threading.Thread(target=l.backward,args=(0.003, 512))
                t1.start()
                t2 = threading.Thread(target=r.backward,args=(0.003, 512))
                t2.start()
            else:
                print('command is wrong!')
    except KeyboardInterrupt:
        GPIO.cleanup();
