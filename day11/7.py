class cat(object):
	def __init__(self,name,color='白色'):
		self.name=name
		self.color=color

	def run(self):
		print('%s--在跑'%self.name)

class bosi(cat):
	def setnewname(self,newname):
		self.name=newname

	def eat(self):
		print('%s--在吃'%self.name)

bs=bosi('印度猫')
print('bs的名字为：%s'%bs.name)
print('bs的颜色为：%s'%bs.color)
bs.eat()
bs.setnewname('波斯猫')
bs.run()
