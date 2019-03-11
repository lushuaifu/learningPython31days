from multiprocessing import Process,Queue
import os, time,random

def write(q):
    for value in ['A','B','C']:
        print('put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value=q.get(True)
            print('get %s from queue '%value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print('')
    print('所有数据都写入，并且读完')