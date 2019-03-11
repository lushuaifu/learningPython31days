# 抽象产品类角色
class Car:
    def move(self):
        pass
    def stop(self):
        pass


# 具体产品类角色
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






# 工厂父类:抽象工厂类角色
class CarFactory(object):
    def createCar(self):
        pass

# 工厂子类：具体工厂类角色
class YiLanTeCarFactory(CarFactory):
    def createCar(self):
        return YiLanTe()

# 工厂子类：具体工厂类角色
class SuoNaTaCarFactory(CarFactory):
    def createCar(self):
        return SuoNaTa()

# 工厂子类：具体工厂类角色
class TuShengCarFactory(CarFactory):
        def createCar(self):
            return TuSheng()


# 客户端
f1 = YiLanTeCarFactory()
car1 = f1.createCar()
car1.move()

f1 = SuoNaTaCarFactory()
car1 = f1.createCar()
car1.move()

f1 = TuShengCarFactory()
car1 = f1.createCar()
car1.move()




