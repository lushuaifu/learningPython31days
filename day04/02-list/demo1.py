#定义了一个list
names = ['唐三藏','孙悟空','猪八戒','沙和尚']
print(names)
#获取list中第一个值
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#下表越界IndexError: list index out of range
#print(names[4])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])
#print(names[-5])
#获取list的长度
num = len(names)
print(num)
#循环打印
index = 0
while index<len(names):
	print(names[index])
	index+=1

print('-'*20)

myList = [110,'旺财',True,3.14,None,'旺财']
index = 0
while index<len(myList):
	print(myList[index])
	index+=1

myList=[]
print(type(myList),len(myList))