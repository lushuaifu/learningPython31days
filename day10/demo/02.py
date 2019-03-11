'''
	定义一个类
		类名：Car
		属性：？
		方法：
			def 名(self):
				方法体
	



	class 类名:
		def 方法名(self):
			方法体
		
		def 方法名(self,参数):
			方法体
	
	对象名　＝　类名()
	对象名　＝　类名()
	对象名　＝　类名()
'''
class Car:
	def run(self):
		print('汽车在奔跑')

baoshijie = Car()
baoshijie.run()
baoshijie.color = 'red'
baoshijie.pailiang = '10T'
print('颜色:%s,排量:%s'%(baoshijie.color,baoshijie.pailiang))
