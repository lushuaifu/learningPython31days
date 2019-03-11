class C1:
    def f1(self):
        print('C1...f1')
class C2:
    def f2(self):
        print('C2...f2')
    def hehe(self):
        print('C2...hehe')
class C3:
    def f3(self):
        print('C3...f3')
    def haha(self):
        print('C3...haha')
    def hehe(self):
        print('C3...hehe')
class C4(C2):
    def f4(self):
        print('C4...f4')
    def haha(self):
        print('C4...haha')
class C5(C4,C3):
    def f5(self):
        print('C5...f4')
    '''
    def hehe(self):
        print('C5...hehe')
    '''

c5 = C5()
c5.haha()
c5.hehe()
