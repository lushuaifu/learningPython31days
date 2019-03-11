'''
匿名
'''

'''
def f1(xx):
	xxx
	return ....
'''
def f1(a,b):
	return a+b

ret = f1(1,2)
print(ret)

f1 = lambda a,b:a+b
ret = f1(1,2)
print(ret)


f1 = lambda a,b:print('a')
f1(1,2)


f1 = lambda:print('a')
f1()


from functools import reduce

ret = reduce(lambda x,y:x+y, [1, 3, 5, 7, 9])
print(ret)

