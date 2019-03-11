'''
抽象类和接口：
这两个类里的方法，没有实现，只有方法的声明

abstract class Aniaml{
    abstract void eat(){}
}
子类实现抽象类的抽象方法
interface Animal{
    static abstract void eat(){}
}
实现类实现接口的抽象方法

以抽象类为例
class Dog extends Animal{
    public void eat(){
        print("dog...eat...")
    }
}
class Cat extends Animal{
    public void eat(){
        print("cat...eat...")
    }
}

'''


# 抽象产品类角色
class Car:
    def move(self):
        pass

    def stop(self):
        pass


# 具体产品角色
class YiLanTe(Car):
    def move(self):
        print('YiLanTe...move...')

    def stop(self):
        print('YiLanTe...stop...')


# 具体产品类角色
class SuoNaTa(Car):
    def move(self):
        print('SuoNaTa...move...')

    def stop(self):
        print('SuoNaTa...stop...')


# 具体产品类角色
class TuSheng(Car):
    def move(self):
        print('TuSheng...move...')

    def stop(self):
        print('TuSheng...stop...')


# 工厂类角色
class CarFactory:
    def createCar(self, typeName):
        car = None
        if typeName == '伊兰特':
            car = YiLanTe()
        elif typeName == '索纳塔':
            car = SuoNaTa()
        elif typeName == '途胜':
            car = TuSheng()
        return car


# 客户端，调用开始。。。。主代码从这里开始
factory = CarFactory()
car = factory.createCar('伊兰特')
car.move()

car = factory.createCar('索纳塔')
car.move()

car = factory.createCar('途胜')
car.move()
