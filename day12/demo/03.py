#Cat类   父类-基类
class Cat:
    def __init__(self,name,color='白色'):
        print('cat...init...')
        self.name = name
        self.color = color

    def run(self):
        print('%s\t奔跑。。。'%self.name)




#BoSiMao类 子类-派生类
class BoSiMao(Cat):
    def __init__(self):
        print('BoSiMao...init...')
    def eat(self):
        print('%s\t吃鱼.......'%self.name)
    def setName(self,name):
        self.name = name





 
b1 = BoSiMao()
