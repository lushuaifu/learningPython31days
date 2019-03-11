import threading
import time

# 全局变量
g_num = 0


# 函数1
def test1():
    global  g_num
    for i in range(1000000):
        #g_num += 1
        g_num = g_num+1
    print("---test1---g_num=%d" % g_num)

# 函数2
def test2():
    global g_num
    for i in range(1000000):
        #g_num += 1
        g_num = g_num + 1
    print("---test2---g_num=%d" % g_num)


def main():
    #创建线程
    t1 = threading.Thread(target=test1)
    #就绪
    t1.start()

    # 创建线程
    t2 = threading.Thread(target=test2)
    # 就绪
    t2.start()


    time.sleep(5)
    print("---main---g_num=%d" % g_num)

if __name__ == '__main__':
    main()


'''
1、打印的顺序
2、为啥最后结果不是2000000
'''
