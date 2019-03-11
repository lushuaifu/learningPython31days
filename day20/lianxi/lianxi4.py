from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print('reader启动(%s),父进程为(%s)'%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print('reader从Queue获取到消息：%s'%q.get(True))

def writer(q):
    print('writer启动(%s)父进程为(%s)'%(os.getpid(),os.getppid()))
    for i in 'zhouge':
        q.put(i)

if __name__=='__main__':
    print('(%s)start'%os.getpid())
    q=Manager().Queue()
    po=Pool()
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print('(%s) end'%os.getpid())
