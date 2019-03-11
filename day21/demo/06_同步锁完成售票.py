# Python主要通过标准库中的threading包来实现多线程
import threading
import time
import os


def doChore():  # 作为间隔  每次调用间隔0.5s
    time.sleep(0.5)


def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                      # 得到一个锁，锁定
        if i != 0:
            i = i - 1                       # 售票 售出一张减少一张
            print(tid, ':now left:', i)    # 剩下的票数
            doChore()
        else:
            print("Thread_id", tid, " No more tickets")
            os._exit(0)                     # 票售完   退出程序
        lock.release()                      # 释放锁
        doChore()


#全局变量
i = 15                      # 初始化票数
lock = threading.Lock()     # 创建锁


def main():
    # 总共设置了3个线程
    for k in range(3):
        # 创建线程; Python使用threading.Thread对象来代表线程
        new_thread = threading.Thread(target=booth, args=(k,))
        # 调用start()方法启动线程
        new_thread.start()

if __name__ == '__main__':
    main()
