from multiprocessing import Process
import time
import os

def worker_1(interval):
    print('worker_1,父进程(%s),当前进程(%s)'%(os.getppid(),os.getpid()))
    t_start=time.time()
    time.sleep(interval)
    t_end=time.time()
    print('worker_1,执行时间为 %0.2f 秒'%(t_end-t_start))

def worker_2(interval):
    print('worker_2,父进程(%s),当前进程(%s)'%(os.getppid(),os.getpid()))
    t_start=time.time()
    time.sleep(interval)
    t_end=time.time()
    print('worker_2,执行时间为 %0.2f 秒'%(t_end-t_start))
if __name__=='__main__':
    print('进程ID：%s'%os.getpid())
    p1=Process(target=worker_1,args=(2,))
    p2=Process(target=worker_2,args=(1,))
    p1.start()
    p2.start ()
    print('p2.is_alive=%s'%p2.is_alive())
    print('p1.name=%s'%p1.name)
    print('p1.pid=%s'%p1.pid)
    print('p2.name=%s'%p2.name)
    print('p2.pid=%s'%p2.pid)
    p1.join()
    print('p1.is_alive=%s'%p1.is_alive())

