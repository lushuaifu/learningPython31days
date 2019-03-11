import time
class animal(object):
	
	def __init__(self,name):
		print('__init__方法被调用')
		self.__name=name

	def __del__(self):
		print('__del__方法被调用')
		print('%s对象马上被干掉。。。'%self.__name)

dog=animal('哈皮狗')
del dog
print('='*20)
cat=animal('波斯猫')
print('_'*20)
cat2=cat
print('2'*10)
cat3=cat
print('1'*10)

print('__马上删除cat对象')
del cat

print('__马上删除cat2对象')
del cat2

print('__马上删除cat3对象')
del cat3

print('程序5秒后结束')
time.sleep(5)
