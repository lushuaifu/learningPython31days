'''
这个文件放在某个文件夹下，表示这个文件夹是一个python的包

__all__ 限定在from 包名 import *的时候，能导入哪些py文件(模块文件)

还可以写一些代码，在初始化这个包的时候，加入一些业务逻辑
'''
#__all__ = ['a','b']

'''
print('__init__    执行了。。。。。。')
def f():
	print('f()......')

f()
'''
from . import a
from ab import b