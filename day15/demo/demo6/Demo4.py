class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

qian = Money()
print(qian.getMoney())
qian.setMoney('100')
print(qian.getMoney())
#print(qian._Money__money)
#print(dir(qian))

