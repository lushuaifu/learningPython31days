import multiprocessing
import os


def run():
        print('run.......')


if __name__ == '__main__':
    print('1......')
    # 创建了一个进程对象       状态：新建状态
    p = multiprocessing.Process(target=run,name='万人迷')

    # 启动：                   状态：就绪状态
    p.start()
    print(p.name)
    p.join()
    print(p.name)
    print('2......')
