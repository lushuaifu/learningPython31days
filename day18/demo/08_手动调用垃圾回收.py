import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))
    # def __del__(self):
    #     print('object del,id:%s'%str(hex(id(self))))

def f3():
    print("-----0------")
    print(gc.collect())
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print("-----1------")
    del c1
    del c2
    print("-----2------")
    print(gc.garbage)
    print("-----3------")
    print(gc.collect()) #显式执行垃圾回收
    print("-----4------")
    print(gc.garbage)
    print("-----5------")

if __name__ == '__main__':
    gc.set_debug(gc.DEBUG_LEAK) #设置gc模块的日志
    f3()


