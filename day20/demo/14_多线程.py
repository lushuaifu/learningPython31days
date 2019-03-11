import threading
import time

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        #创建子线程，子线程执行的功能方法是saySorry
        t = threading.Thread(target=saySorry)
        # 启动线程，即让线程开始执行
        t.start()


