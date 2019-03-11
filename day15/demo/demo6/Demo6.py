'''
私有的属性，为了对外能访问，提供了对外访问的get,set方法
但是对于使用的时候稍微繁琐，使用  ret= property(get,set)
当对象获取ret的时候，相当于调用了get方法，获取返回值
当对象设置ret的时候，相当于调用set,将设置的值传递给set的方法作为实参

相当于一个伪装


@注解，get,set方法名字保持一致xx，在当时的get方法头部加 @property,在原来的set方法头部加@xx.setter
'''

class Money(object):

    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        print('getMoney...')
        return self.__money
    @money.setter
    def money(self, value):
        print('setMoney...')
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")




qian = Money()
print(qian.money)
qian.money = 100
print(qian.money)

