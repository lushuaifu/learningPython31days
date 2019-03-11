'''
可变参数的一种，*组成成元组，**组成字典
'''
def f1(a,b,**kw):
	print(a,b,kw)

f1(1,2,id=1,name='zs')


def f1(a,*args,**kw):
	print(a,args,kw)

f1(1,2,3,4,5,id=1,name='zs')

def f1(a,*args,**kw):
	print(a,args,kw)

f1(1,2,3,4,5)