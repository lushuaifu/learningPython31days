'''
try:
    可能发生异常的代码
except 描述异常的类:
    处理异常的代码块
'''

'''
try:
    print('-----test--1---')
    open('123.txt', 'r')
    print('-----test--2---')
except Exception:
    print('except...')
print('over...')
'''


try:
    print('-----test--1---')
    open('123.txt', 'w')
    print('-----test--2---')
    num = 10/0
    print('-----test--3---')
except (FileNotFoundError,ZeroDivisionError):
    print('except...')
print('over...')



print('*'*100)
try:
    print('-----test--1---')
    open('123.txt', 'w')
    print('-----test--2---')
    num = 10/0
    print('-----test--3---')
except:
    print('except...')
print('over...')

