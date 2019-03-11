import threading
from time import sleep,ctime

def sing():
    print(threading.current_thread().name)
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    print(threading.current_thread().name)
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    #哪个线程运行，就获取哪个线程对象的名字
    print(threading.current_thread().name)

    print('---开始---:%s'%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    #sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
    print('---结束---:%s'%ctime())
