s1={'1001':'旺财','1002':'小强','1003':'阿黄'}
s2=s1.copy()
print(s1,s2,id(s1),id(s2))

s3=s1.fromkeys(['1','2','3'],'哈哈')
print(s3)
print()

s2={'1001':'旺财','1002':'小强','1003':'阿黄'}
s4=s2.fromkeys(['1','2','3','哈哈','嘿嘿','xxx'])
print(s4)
s1.setdefault('1111')
print(s1)
s1.setdefault('1122','xxx')
print(s1)

s1={'1001':'旺财','1002':'小强','1003':'阿黄'}
s2={'1456':'小明'}
s1.update(s2)
print(s1,s2)
