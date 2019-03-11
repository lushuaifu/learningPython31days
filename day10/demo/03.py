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



	self:谁调用这个方法，就是谁．
'''
class Car:
	def run(self):
		print('汽车在奔跑')
		
	def show(self):
		print('颜色:%s,排量:%s'%(self.color,self.pailiang))


baoshijie = Car()
baoshijie.run()
baoshijie.color = 'red'
baoshijie.pailiang = '10T'
baoshijie.show()

qq = Car()
qq.run()
qq.color='white'
qq.pailiang = '1T'
qq.num=4
qq.show()

print('baoshijie.num:%s'%(baoshijie.num))
print('qq.num:%s'%(qq.num))

