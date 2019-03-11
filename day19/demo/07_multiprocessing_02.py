import multiprocessing
import os


def run(*args):
    print('子进程运行中，name= %s ,pid=%d...ppid=%s' % (args[0], os.getpid(),os.getppid()))


if __name__ == '__main__':
    print('1......')
    # 创建了一个进程对象       状态：新建状态
    p = multiprocessing.Process(target=run,args=('进程1','xx'))
    # 启动：                   状态：就绪状态
    p.start()
    print('2......pid=%s'%os.getpid())


