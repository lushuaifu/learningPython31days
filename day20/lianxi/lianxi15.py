import threading
import time

class myThread(threading.Thread):
    def __init__(self,num,sleepTime):
        threading.Thread.__init__(self)
        self.num=num
        self.sleepTime=sleepTime

    def run(self):
        self.num+=1
        time.sleep(self.sleepTime)
        print('线程(%s),num=%d'%(self.name,self.num))

if __name__=='__main__':
    mutex=threading.Lock()
    t1=myThread(100,5)
    t1.start()
    t2=myThread(200,1)
    t2.start()

