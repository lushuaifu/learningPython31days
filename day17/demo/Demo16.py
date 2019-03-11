class Dog:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

wangcai = Dog('旺财','哈巴狗')
print(dir(wangcai))

wangcai.weight = 20
print(dir(wangcai))

del wangcai.weight
print(dir(wangcai))
