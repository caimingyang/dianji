import threading
from kafka import KafkaConsumer, TopicPartition, KafkaProducer
from sdk.Dianji import Dianji
class KafkaReceiver: 
    scan ="false"
    dianji = Dianji()
    def setDianji(self,d):
        self.dianji = d
    def createThread(self):
        t2 = threading.Thread(target=self.receiveScanMsg,args=())
        t2.start()

    def receiveScanMsg(self):
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
        consumer.subscribe('scan')
        print('receiveScanMsg consumer connected')
        for msg in consumer:
            self.scan=msg.value.decode()
            print(self.scan)
            record = self.dianji.getRecord()
            left='left'
            right='right'
            forward='forward'
            backward ='backward'
            print(record)
            if record > 25:
                producer.send('car', left.encode())
            elif record < -25:
                producer.send('car', right.encode())
            else:
                producer.send('car', forward.encode())

    def getScan(self):
        return self.scan
