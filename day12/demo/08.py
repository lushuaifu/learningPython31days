class GodfatherOne:
    def geiqian(self):
        print('给钱......')
    def geiming(self):
        print('给名2......')
   

class GodfatherTwo:
    def geiming(self):
        print('给名......')


class Goddaughter(GodfatherOne,GodfatherTwo):
    def maibao(self):
        print('买包。。。。。。。')




guomeimei = Goddaughter()
guomeimei.geiqian()
guomeimei.geiming()
guomeimei.maibao()

#获取此类继承的父类结构
print(Goddaughter.__mro__)
