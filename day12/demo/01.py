'''
    1、定义一个类，Cat
        属性：
            name,color
        方法：
            run
    2、定义一个类：继承Cat,起名BoSiMao
        
        定义自己特有的内容：
            属性：
                ？
            方法：
                ？

'''
#Cat类   父类-基类
class Cat:
    def __init__(self,name,color='白色'):
        print('self:%s,id:%s'%(self,id(self)))
        self.name = name
        self.color = color

    def run(self):
        print('%s\t奔跑。。。'%self.name)

#BoSiMao类 子类-派生类
class BoSiMao(Cat):
    pass

 
b1 = BoSiMao('花花')
print(b1.name)
b1.run()

#打印对象的地址
print(id(b1))

