class dog:
	def __init__(self,new_name,new_brand):
		print('_'*10)
		self.name=new_name
		self.brand=new_brand
	def show(self):
		print('名字：%s,品种：%s'%(self.name,self.brand))
wangcai=dog('旺财','哈士奇')
wangcai.show()

xiaoqiang=dog('小强','泰迪')
xiaoqiang.show()
