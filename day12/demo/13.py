class Father:
    def f1(self):
        print('Father...f1...')
    def f2(self):
        print('Father...f2...')
    def f3(self):
        print('Father...f3...')
        self.f2()

class Son(Father):
    def f1(self):
        print('Son...f1...')
    def f2(self):
        print('Son...f2...')

#匿名对象
Son().f3()
#Son().f1()

#s = Son()
#s.f3()
#s.f2()
