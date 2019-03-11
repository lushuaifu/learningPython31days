
class Singleton(object):
    #表示对象是否被创建 None:没有，其它：已经创建
    __instance = None
    #表示是否是第一次调用init,False:不是第一次   True:是第一次
    __first_init = True
    def __init__(self,*args,**kwargs):
        if Singleton.__first_init:
            self.args = args
            self.kwargs = kwargs
            Singleton.__first_init = False
    def __new__(cls,*args,**kwargs):
        if cls.__instance==None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

#wangcai = Singleton('旺财')
#wangcai = Singleton()
#wangcai = Singleton(1,2,3,4)
wangcai = Singleton(name='abc')

print(wangcai.args)
print(wangcai.kwargs['name'])