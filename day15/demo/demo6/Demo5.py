'''
私有的属性，为了对外能访问，提供了对外访问的get,set方法
但是对于使用的时候稍微繁琐，使用  ret= property(get,set)
当对象获取ret的时候，相当于调用了get方法，获取返回值
当对象设置ret的时候，相当于调用set,将设置的值传递给set的方法作为实参

相当于一个伪装
'''

class Money(object):

    def __init__(self):
        self.__money = 0

    def getMoney(self):
        print('getMoney...')
        return self.__money

    def setMoney(self, value):
        print('setMoney...')
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    money = property(getMoney, setMoney)


qian = Money()
print(qian.money)
qian.money = 100
print(qian.money)

