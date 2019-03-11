import threading
import time

# 全局变量
g_num = 0
myLock = threading.Lock()


# 函数1
def test1():
    global  g_num
    # 上锁
    myLock.acquire()
    print('test1...上锁...')
    for i in range(1000000):
        g_num = g_num+1
    # 开锁
    myLock.release()
    print('test1...开锁...')
    print("---test1---g_num=%d" % g_num)

# 函数2
def test2():
    print('test2...')
    global g_num
    myLock.acquire()
    #time.sleep(2)
    print('test2...上锁...')
    for i in range(1000000):
        g_num = g_num + 1
        # 开锁
    myLock.release()
    print('test2...开锁...')
    print("---test2---g_num=%d" % g_num)


def main():
    #创建线程
    t1 = threading.Thread(target=test1)
    #t1 = threading.Thread(target=test1,args=(myLock,))
    #就绪
    t1.start()


    # 创建线程
    t2 = threading.Thread(target=test2)
    # 就绪
    t2.start()
    print("---main---g_num=%d" % g_num)

if __name__ == '__main__':
    main()


