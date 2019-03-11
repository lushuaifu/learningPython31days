def fun1(a,b,c='默认值',*d,**e):	
	print(a,b,c,d,e)

fun1(1,2,3,44,55,id=1,name='haha')
#1 2 3 (44, 55) {'name': 'haha', 'id': 1}

def fun1(a,b=110,c='默认值',*d,**e):	
	print(a,b,c,d,e)

fun1(1,2,33,44,id=1,name='haha')
#1 2 33 (44,) {'id': 1, 'name': 'haha'}


def fun1(a,b=110,c='默认值'):	
	print(a,b,c)

fun1(1,2,3)
fun1(1,c=2)
#1 2 3
print('xx',end='-')
print('xx','-')
print('yy')
help(print)