'''
    1、房
            属性：
                面积int，家具list


            方法：
                放家具的方法(面积的判断，剩余面积的计算)


    2、家具

            属性：
                面积int，名字str

'''
#家具类
class Furniture:
    #初始化
    def __init__(self,area,name):
        self.area = area
        self.name = name
    #转字符串
    def __str__(self):
        msg = '家具的名字是%s,面积是%s.'%(self.name,self.area)
        return msg

#房类
class Home:
    #初始化
    def __init__(self,area):
        self.area = area
        self.furnitures = []

    #转字符串
    def __str__(self):
       #总面积
       sumArea = self.area
       #描述家具的名字
       fs = '家具是:'
       if len(self.furnitures)!=0:
           for f in self.furnitures:
               sumArea+=f.area
               fs = fs+f.name+','
           fs=fs.rstrip(',')
           msg = '家的总面积是:%s,剩余面积是:%s.%s'%(sumArea,self.area,fs)
       else:
           msg = '家的总面积是:%s,剩余面积是:%s'%(sumArea,self.area)
       return msg

    #放家具
    def putFurniture(self,furniture):
        if self.area >= furniture.area:
            self.area -= furniture.area
            self.furnitures.append(furniture)
            print('家具%s放入成功'%furniture.name)
        else:
            print('家具过大，放不下.当前的剩余面积是%s,家具的面积是%s'%(self.area,furniture.area))



#创建对象

home = Home(120)

bed1 = Furniture(4,'双人床')
#print(bed1)
bed2 = Furniture(200,'N人床')
#print(bed2)
bed3 = Furniture(6,'3人床')




home.putFurniture(bed1)
print(home)
home.putFurniture(bed2)
print(home)
home.putFurniture(bed3)
print(home)



