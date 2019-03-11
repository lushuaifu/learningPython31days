class money(object):
    def __init__(self):
        self.__money=0
    @property
    def xx(self):
        return self.__money
    @xx.setter
    def aa(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print('error:不是整形数字')


a=money()
print(a.xx)
a.aa=100
print(a.xx)


