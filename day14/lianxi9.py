class test(object):
    def __init__(self,switch):
        self.switch=switch   #开关

    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print('捕获开启，已经捕获到了异常，信息如下：')
                print(result)
            else:
                raise

a=test(True)
a.calc(11,0)

print('*'*50)
'''
a.switch=False
a.calc(11,0)
'''
