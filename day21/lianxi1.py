import threading
import time
import os

def dochore():    #作为间隔，每次调用间隔0.5秒
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while 1:
        lock.acquire()
        if i!=0:
            i=i-1
            print(tid,':now left:',i)
            dochore()
        else:
            print('Thread_id',tid,'no more tickets')
            os._exit(0)   #票售完，退出程序
        lock.release()
        dochore()

i=15
lock=threading.Lock()

def main():
    for k in range(3):
        #创建线程；Python使用threading.Thread对象来代表线程
        new_thread=threading.Thread(target=booth,args=(k,))
        new_thread.start()

if __name__=='__main__':
    main()
