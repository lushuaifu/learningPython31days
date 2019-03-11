'''
    定义一个美女类：
        属性：
            1、姓名
            2、年龄
            3、三围
        方法：
            1、逛街
            2、洗衣服
            3、做饭
            4、吵架
            5、生孩子
            6、....
        
'''
class Beauty:
    def __init__(self,name='美女',age=18,bwh=1):
        self.name = name
        self.age = age
        self.bwh = bwh

    def __str__(self):
        msg = '姓名:%s,年龄:%s,三围:%s'%(self.name,self.age,self.bwh)
        return msg

    def shopping(self):
        print('逛。。。。。。')

    def eat(self):
        print('%s吃。。。。。。'%self.name)

yuanyuan = Beauty()
jingjing = Beauty(age=20)
print(yuanyuan)
print(jingjing)

lzl = Beauty('林志玲',40,2)
print(lzl)
lzl.eat()

