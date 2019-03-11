from multiprocessing import Pool
import time
import os


def test():
    print("---进程池中的进程---pid=%d,ppid=%d--" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("----%d---" % i)
        time.sleep(1)
    return "老王"


def test2(args):
    print('1...')
    time.sleep(10)
    print("---callback func--pid=%d" % os.getpid())
    print("---callback func--args=%s" % args)
    print('2...')

if __name__ == '__main__':

    pool = Pool(3)
    #callback表示前面的func方法执行完，再执行callback,并且可以获取func的返回值作为callback的参数
    pool.apply_async(func=test, callback=test2)
    #pool.apply_async(func=test)

    #模拟主进程在做任务
    time.sleep(5)

    print("----主进程-pid=%d.....服务器是不关闭的----" % os.getpid())
    # while True:
    #     pass

