class singleton(object):
    __instance=None
    __first_init=False
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self,age,name):
        if not self.__first_init:
            self.age=age
            self.name=name
            singleton.__first_init=True

a=singleton(18,'wangcai')
b=singleton(8,'wangcai')
print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age=19
print(b.age)