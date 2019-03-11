#coding=utf-8

#修改import中的Queue为Manager
import multiprocessing
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    #time.sleep(1)
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get())

def writer(q):
    print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "yongGe":
        q.put(i)

if __name__=="__main__":
    print("(%s) start"%os.getpid())
    q=multiprocessing.Manager().Queue() #使用Manager中的Queue来初始化
    #q = multiprocessing.Queue()
    po=multiprocessing.Pool(4)
    #使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    # po.apply_async(writer,(q,))
    # po.apply_async(reader,(q,))
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())
