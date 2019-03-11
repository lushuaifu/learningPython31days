class f1:
	def __init__(self,name='西施',age=18):
		self.name=name
		self.age=age

	def __str__(self):
		a='姓名：%s,年龄：%s'%(self.name,self.age)
		return a
	def shopping(self):
		print('%s逛。。。'%self.name)
	def eat(self):
		print('%s吃。。。'%self.name)

xishi=f1()
print(xishi)
xishi.eat()
xishi.shopping()
daiyu=f1(name='黛玉')
print(daiyu)		
