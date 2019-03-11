'''
    多线程共享全局变量，一旦有一个修改，另一个受影响
'''

from threading import Thread
import time

#全局变量
g_num = 100


#修改全局变量
def work1():
    #如果想修改全局变量，必须加global
    global g_num
    for i in range(3):
        g_num += 1

    print("----in work1, g_num is %d---"%g_num)

#获取全局变量
def work2():
    global g_num
    print("----in work2, g_num is %d---"%g_num)


#将功能包装成函数方法
def main():
    print("---线程创建之前g_num is %d---" % g_num)
    #创建一个线程
    t1 = Thread(target=work1)
    #就绪
    t1.start()

    # 延时一会，保证t1线程中的事情做完
    time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()


if __name__ == '__main__':
   #调用方法
   main()