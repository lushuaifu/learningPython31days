'''
    想设计成单例模式：
    object.__new__(cls)只能调用一次

'''
class Singleton(object):
    __instance = None
    def __new__(cls):
        if cls.__instance==None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

wangcai = Singleton()
xiaoqiang = Singleton()

print(wangcai==xiaoqiang)
print(id(wangcai))
print(id(xiaoqiang))