'''
    = ：浅拷贝
    deepcopy : 深拷贝
    copy:   对于列表(深)，对于元组(浅)
            对于里面的对象相当于浅拷贝
'''


import  copy

a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c                       #浅拷贝，c和d指向同一个内存块

e = copy.deepcopy(c)        #深拷贝，递归拷贝里面的信息，都是得到新的

a.append(110)
print(d[0])
print(e[0])


a = [1,2,3]
b = copy.copy(a)            #深拷贝

print(id(a))
print(id(b))
print(a)
print(b)


a = (1,2,3)
b = copy.copy(a)            #浅拷贝

print(id(a))
print(id(b))
print(a)
print(b)




a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c               #浅拷贝
e = copy.copy(c)

print(id(e))
print(id(c))

a.append(110)

print(c)
print(e)
print('*'*100)

a = [1,2,3]
b = [4,5,6]
c = (a,b)
d = c               #浅拷贝
e = copy.copy(c)

a.append(110)

print(id(e))
print(id(c))

print(c)
print(e)
print('*'*100)


a = [1,2,3]
b = a[:]
print(id(a))
print(id(b))



d = dict(name="zhangsan", age=27)
e = copy.copy(d)

print(id(d))
print(id(e))


a  = list(range(1,5))
print(a)