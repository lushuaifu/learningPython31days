'''
    Python 对小整数的定义是 [-5, 257) 这些整数对象是提前建立好的，不会被垃圾回收。
    在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象.
'''

a = 100
b = 100
print(id(a))
print(id(b))

a = 500000000000000000
b = 500000000000000000
print(id(a))
print(id(b))


a = 'a bc'
b = 'a bc'
print(id(a))
print(id(b))