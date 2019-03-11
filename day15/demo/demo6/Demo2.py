'''
浅拷贝：将引用给对方
'''
a = [1,2,3]
b = a

print(id(a))
print(id(b))

a.append(4)
print(b)


a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c
a.append(110)
print(d[0])

'''
import copy

a = [1,2,3]
b = copy.deepcopy(a)
print(id(a))
print(id(b))
'''

a.append(110)
print(b)