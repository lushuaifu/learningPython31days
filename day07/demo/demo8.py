def f1(a,b,c):
	print(a,b,c)

f1(1,2,3)
f1(b=1,a=2,c=3)


def f1(a,b,*,c,d):
	print(a,b,c,d)
f1(1,2,d=3,c=4)

def f1(a,b=444444,*s,c,d):
	print(a,b,s,c,d)
f1(1,2,77,88,c=3,d=4)

#顺序

def myFun(a,b='默认',*arg,**kw):
	print(a,b,arg,kw)

myFun(1,2,3,4,5,id=10,name='wangcai')
myFun(1,id=10,name='wangcai')