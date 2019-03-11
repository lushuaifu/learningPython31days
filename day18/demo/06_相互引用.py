'''
python垃圾回收机制：
    1、引用计数                 主
    2、隔代回收（三代）         辅
'''

import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

#关掉垃圾回收
gc.disable()
#gc.enable()
f2()



