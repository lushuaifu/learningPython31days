class money(object):
    def __init__(self):
        self.__money=0
    def getmoney(self):
        return self.__money
    def setmoney(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print('error:不是整形数字')
    xx=property(getmoney,setmoney)


a=money()
print(a.getmoney())
print(dir(a))
print(a._money__money)
a.setmoney(100)
print(a.getmoney())
a.xx
print(a.xx)
a.xx=200
print(a.xx)


