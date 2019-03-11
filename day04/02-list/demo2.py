myList=[110,'旺财',True,3.14,None,'旺财',[1,2,3]]
print(myList[1])
print(myList[6][2])
#获取3.14在myList中的下标，
#如果有重复，获取第一个
#如果不存在，报错
index1 = myList.index(3.14)
print(index1)
index2 = myList.index('旺财')
print(index2)
#index3 = myList.index('小强')
#print(index3)
#获取出现的次数，没有就是0
c1 = myList.count('旺财')
print(c1)
#list中值的总数
length = len(myList)
print(length)

myList2 = [234,345,12,4,1111]
#最大值最小值
print(max(myList2),min(myList2))

myList2 = ['ab','aeddd','cddfsdfdsf']
print(max(myList2),min(myList2))