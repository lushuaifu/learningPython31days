import multiprocessing
import os
import time


def run(filename):
    print('子进程运行中......filename= %s ,pid=%d...ppid=%s' % (filename, os.getpid(),os.getppid()))
    time.sleep(1)

if __name__ == '__main__':
    print('欢迎来下载......')

    p1 = multiprocessing.Process(target=run,args=('/a/xx.avi',))

    p1.start()

    # A进程运行了这句代码，A就会等待p1执行完毕之后，才会继续往下运行
    p1.join()


    p2 = multiprocessing.Process(target=run, args=("/a/oo.avi",))
    p2.start()
    p2.join()

    p3 = multiprocessing.Process(target=run, args=("/a/pp.avi",))
    p3.start()
    p3.join()




    print('下载完毕了......')


