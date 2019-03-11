import threading
import time

'''
一般来说：就像异常处理一样，加上需要的地方
'''

# 全局变量
g_num = 0
myLock = threading.Lock()


# 函数1
def test1():
    global  g_num

    for i in range(1000000):
        myLock.acquire()
        g_num = g_num+1
        myLock.release()

    print("---test1---g_num=%d" % g_num)

# 函数2
def test2():
    print('test2...')
    global g_num
    for i in range(1000000):
        myLock.acquire()
        g_num = g_num + 1
        myLock.release()
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


