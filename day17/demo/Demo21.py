import types

class Dog:
    __slots__=('name','brand')
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

def eat(self):
        print('eat...')

@classmethod
def he(cls):
    print('he...')


wangcai = Dog('旺财','哈士奇')
print(wangcai.name)
wangcai.color = 'baise'
print(wangcai.color)
wangcai.eat = types.MethodType(eat,wangcai)
wangcai.eat()


# Dog.color = 'xx'
# print(Dog.color)
# Dog.eat = eat
# Dog.he = he
# Dog.he()

wangcai = Dog('旺财','哈士奇')
del wangcai.name
#print(dir(wangcai))
#print(wangcai.name)

