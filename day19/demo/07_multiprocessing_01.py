import multiprocessing
import os
import time


def run():
        for i in range(5):
            time.sleep(1)
            print('run.......ppid=%s'%(os.getppid()))

if __name__ == '__main__':
    print('1......')
    # 创建了一个进程对象       状态：新建状态
    p = multiprocessing.Process(target=run)
    # 启动：                   状态：就绪状态
    p.start()
    print('2......')
