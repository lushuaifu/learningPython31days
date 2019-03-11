import  time

class Dog:
    #表示Dog产生的对象，可以被调用
    def __call__(self,*args,**kwargs):
        print('call。。。')
        print(args)
        print(kwargs)

wangcai = Dog()
time.sleep(2)
wangcai('骨头','狗粮',111)

time.sleep(2)

xiaoqiang = Dog()
xiaoqiang()