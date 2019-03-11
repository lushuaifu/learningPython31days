class People(object):
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls,country):
        cls.country = country


    def haha(self):
        print('haha')

    @staticmethod       
    def hehe():
        print('hehe')


p = People()
p.haha()
p.hehe()
People.hehe()
