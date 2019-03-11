'''
    想设计成单例模式：
    object.__new__(cls)只能调用一次

'''
class Singleton(object):
    #表示对象是否被创建 None:没有，其它：已经创建
    __instance = None
    #表示是否是第一次调用init,False:不是第一次   True:是第一次
    __first_init = True
    def __init__(self,name):
        if Singleton.__first_init:
            self.name = name
            Singleton.__first_init = False
    def __new__(cls,name):
        if cls.__instance==None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

wangcai = Singleton('旺财')
xiaoqiang = Singleton('小强')


print(wangcai==xiaoqiang)
print(id(wangcai))
print(id(xiaoqiang))

print(wangcai.name)
print(xiaoqiang.name)