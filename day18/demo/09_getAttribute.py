class Test(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # def __getattribute__(self, obj):
    #     print('__getattribute__...')
    #     #return 'xx'
    #     return object.__getattribute__(self, obj)
    #属性访问时拦截器，打log
    def __getattribute__(self,obj):
        if obj == 'subject1':
            print('if...')
            return 'xx'
        else:   #测试时注释掉这2行，将找不到subject2
            print('else...')
            return object.__getattribute__(self,obj)
            #return self.subject1

    def show(self):
        print('this is Test')

s = Test("python")
#print(s.subject1)
#print(s.subject2)
s.show()
