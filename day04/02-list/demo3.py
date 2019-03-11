ls = [1,2,'abc',None,False,True]
print(ls.count(1))
print(ls.count(0))
'''
#count的实现原理
value=1
i = 0
num = 0
while i<len(ls):
	if ls[i]==value:
		num+=1
	i+=1
print('次数%d'%num)
'''

print(''==False)
print(None==False)
print(0==False)

