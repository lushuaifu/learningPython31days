'''
    当子类的方法和父类的方法名一致的时候，子类的方法覆盖或者重写父类的方法
'''


class Father:
    def haha(self):
        print('father...haha....')

class Son(Father):
    def haha(self):
        print('son...haha....')

son = Son()
son.haha()
