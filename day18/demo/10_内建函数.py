ret = range(0,10,3)
for i in ret:
    print(i)

print('*'*100)

import  collections
map1 = map(lambda x:x*x,[1,2,3])
print(isinstance(map1,collections.Iterable))
for i in map1:
    print(i)

map2 = map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
for i in map2:
    print(i)

def f1( x, y ):
    return (x,y)

l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
map3 = map( f1, l1, l2 )
for i in map3:
    print(i)

ret = filter(lambda x: x%2, [1, 2, 3, 4])
print(ret)
print(isinstance(ret,collections.Iterable))
for i in ret:
    print(i)

ret = filter(None, [1, 2, 3, 4])
for i in ret:
    print(i)

import functools

print(dir(functools))
ret = functools.reduce(lambda x, y: x+y, [1,2,3,4,5])
print(ret)

def f(x,y):
    print('x=%s,y=%s'%(x,y))
    return x+y

#ret = functools.reduce(lambda x, y: x+y, ['a','b','c','d'],'o')
ret = functools.reduce(f, ['a','b','c','d'],'o')
print(ret)

ret = functools.reduce(lambda x, y: x-y, [1,2],10)
print(ret)

'''
排序
'''

'''
ls = [1,233,44,10,2]
ls.sort()
print(ls)
'''

'''
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable,key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

>>>
'''

'''
ls = [1,233,44,10,2]
ls = sorted(ls)
print(ls)
ls = sorted(ls,reverse=True)
print(ls)
'''


'''
ls = [['b',3],['c',1],['a',2]]
print(sorted(ls,key=lambda x:x[1],reverse=True))
print(sorted(ls,key=lambda x:x[1]))
'''

students = {'101':['b',3],'1000':['c',1],'500':['a',2]}
print(sorted(students))
print(sorted(students.items(),key=lambda x:x[0]))
print(sorted(students.items(),key=lambda x:x[1][1]))
'''
sorted(一个参数)

ls = [1,233,44,10,2]
for i in ls:
	print(i)

students = {'100':['b',3],'1000':['c',1],'500':['a',2]}
for i in students:
	print(i)

'''

students = {'101':['b',3],'1000':['c',1],'500':['a',2]}
for i in students.items():
	print(i)


class Dog:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return 'Dog : name=%s,weight=%s'%(self.name,self.weight)


d1 = Dog('狗1',10)
d2 = Dog('狗2',20)
d3 = Dog('狗3',9)
d4 = Dog('狗4',18)

ls = [d1,d2,d3,d4]
print(ls)

for i in ls:
    print(i)

ls = sorted(ls,key=lambda x:x.weight)
for i in ls:
    print(i)