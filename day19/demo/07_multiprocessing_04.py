from multiprocessing import Process
import os
from time import sleep

# 子进程要执行的代码
def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age,os.getpid()))
        print(kwargs)
        sleep(0.5)

if __name__=='__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
    print('子进程将要执行')
    p.start()
    sleep(1)
    #terminate此进程的任务结束
    #p.terminate()
    #print(p.is_alive())
    p.join()
    #print(p.is_alive())
    print('子进程已结束')
