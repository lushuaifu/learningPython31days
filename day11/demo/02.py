'''
    烤地瓜：
        1、属性
                1、分钟数                       数字
                    0-3生的
                    3-5半生
                    5-8熟
                    8—木炭
                2、说明                         字符串
                    生，半生，熟，木炭

                3、调料                        列表集合



        2、方法

                1、烤
                    参数    时间
                    随着时间的增加，说明也得改变

                2、加调料
                    列表增加值   list.append




        3、__init__   __str__

            __init__:
                初始化参数
            __str__:
                打印红薯的状态说明，如果有调料，打印调料。
                打印地瓜的说明，还有调料





'''

#定义类
class Potato:
    #定义__init__
    def __init__(self,cookedLevel=0,cookedString='生',condiments=[]):
        self.cookedLevel = cookedLevel
        self.cookedString = cookedString
        self.condiments = condiments
    
    #定义__str__
    def __str__(self):
        msg = '烤了%s分钟，现在的状态是%s.'%(self.cookedLevel,self.cookedString)
        if len(self.condiments)!=0:
            condimentsString = '调料是:' 
            '''
            for i in self.condiments:
               condimentsString = condimentsString+i+','
            msg = msg+condimentsString.rstrip(',')
            '''
            msg = msg+condimentsString+','.join(self.condiments)
        return msg

    #cook方法
    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel<=3:
            self.cookedString = '生'
        elif self.cookedLevel<=5:
            self.cookedString = '半生'
        elif self.cookedLevel<=8:
            self.cookedString = '熟'
        else:
            self.cookedString = '木炭'
        print('又烤了%s分钟，现在总共烤了%s分钟，现在的状态是%s'%(time,self.cookedLevel,self.cookedString))
    #加调料
    def addCondiments(self,condiment):
        self.condiments.append(condiment)


#创建对象
potato1 = Potato()

potato1.cook(5)
print(potato1)

potato1.cook(2)
potato1.addCondiments('番茄酱')
potato1.addCondiments('芝麻酱')
potato1.addCondiments('辣椒')
print(potato1)

potato1.cook(3)
print(potato1)
        






    
        





















