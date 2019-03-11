class Dog:
    color = 'xxx'
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    def eat(self):
        pass


#del Dog.color
#delattr(Dog,'color')
print(Dog.color)
wangcai = Dog('旺财','哈巴狗')
print(wangcai.name)

#del wangcai.eat
#delattr(wangcai,'eat')

wangcai.eat()

#del wangcai.name
#delattr(wangcai,'name')
#print(wangcai.name)



