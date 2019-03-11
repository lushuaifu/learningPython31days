'''
    当子类的方法和父类的方法名一致的时候，子类的方法覆盖或者重写父类的方法
    如果在子类中想调用父类被重写的方法
            super().父类的方法名()
            父类名.父类的方法名(self)
'''


class Father:
    def haha(self):
        print('father...haha....')
class Father2:
    def haha(self):
        print('father2...haha....')

class Son(Father,Father2):
    def haha(self):
        print('son...haha....')
        print(super())
        print(id(super()))
        print(self)
        print(id(self))
        super().haha()
    def hehe(self):
        print('son...hehe....')
        #super().haha()
        Father2.haha(self)

son = Son()
#son.haha()
son.hehe()

