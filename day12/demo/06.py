class Father:
    def __init__(self):
        self.__name = '爹'
    def chouyan(self):
        print('抽烟')
    def __hejiu(self):
        print('喝酒')
    def tangtoufa(self):
        print('烫头发')


class Son(Father):
    pass



wangcai = Son()
wangcai.chouyan()
print(wangcai.__name)
