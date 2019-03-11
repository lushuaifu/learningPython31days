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