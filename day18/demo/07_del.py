'''
当对象被当做垃圾回收的时候，才会调用对象del方法，然后释放内存
一般不要重写__del__
'''

import  time

class Dog(object):
    def __del__(self):
        #python解析器在调用这个方法的时候，会释放资源
        print('del...')



d1 = Dog()
d2 = d1

del d1
del d2



time.sleep(6)