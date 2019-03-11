'''
try:
    可能发生异常的代码
except 描述异常的类:
    处理异常的代码块
'''



try:
    print('-----test--1---')
    open('123.txt', 'r')
    print('-----test--2---')
    num = 10/0
    print('-----test--3---')
except (FileNotFoundError,ZeroDivisionError) as ex:
    print('except...')
    print(type(ex))
    print(ex)
    print(str(ex))
print('over...')

