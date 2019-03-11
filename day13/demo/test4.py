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


# 定义一个销售北京现代车的店类
class CarStore(object):
    def order(self, factory):
        return factory.createCar()


# 工厂父类:抽象工厂类角色
class CarFactory(object):
    def createCar(self):
        pass


class YilanteCarFactory(CarFactory):
    def createCar(self):
        return YiLanTe()


class SuonataCarFactory(CarFactory):
    def createCar(self):
        return SuoNaTa()


# 客户端
cs = CarStore()
car = cs.order(YilanteCarFactory())
car.move()


car = cs.order(SuonataCarFactory())
car.move()

