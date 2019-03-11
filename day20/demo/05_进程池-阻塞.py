from multiprocessing import Pool
import os,time,random

'''
    阻塞式：相当于单任务
        任务一个一个执行，按照放入的顺序
'''

def worker(msg):
    time.sleep(random.random() * 2)
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))
if __name__ == '__main__':
    po=Pool(4)
    for i in range(0,10):
        po.apply(worker,(i,))
    print("----start----")
    po.close()
    po.join()
    print("-----end-----")
