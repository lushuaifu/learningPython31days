'''
#定义字典，里面存储3个键值对
students={'1001':'旺财','1002':'小强','1003':'小明'}
#判断
id = input('输入学号:')
hasKey = id in students
print(hasKey)
'''




students={'1001':'旺财','1002':'小强','1003':'小明'}
for k in students:
	print(k,students[k])

print(students.keys(),type(students.keys()))

for k in students.keys():
	print(k,students[k])

for k,v in students.items():
	print(k,v)


print(students.items())
a,b = 10,20
print(a,b)


a,b = (10,20)
print(a,b)


s1 = {'1001':'旺财','1002':'小强','1003':'小明'}
#复制并得到一个新的字典，内容和原字典一样，地址不一样
s2 = s1.copy()
print(s1,s2,id(s1),id(s2))
#将一个集合的值作为键，可以字典的默认值
d1 = dict.fromkeys(['1001','1002','1003'])
print(d1)

d1 = dict.fromkeys(['1001','1002','1003'],'哈哈')
print(d1)
d1 = dict.fromkeys(s1.keys(),'哈哈')
print(d1)


s1 = {'1001':'旺财','1002':'小强','1003':'小明'}
print(s1,id(s1))
s1.setdefault('11111')
print(s1,id(s1))
s1.setdefault('11112','xxxx')
print(s1,id(s1))

s1 = {'1001':'旺财','1002':'小强','1003':'小明'}
s2 = {'name':'张三'}
s1.update(s2)
print(s1,s2)

#setdefault通过键获取值，如果键不存在，设置key:None
s1={'1001':'旺财','1002':'小强','1003':'小明'}
print(s1.get('1001'))
print(s1.get('1004'))
print(s1.get('1004','xx'))
print(s1.setdefault('1001'))
print(s1.setdefault('1004'),s1)
print(s1.setdefault('1005','xx'),s1)