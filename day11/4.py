class home:
	def __init__(self,area):
		self.area=area
		self.light='on'
		self.containsitem=[]
	
	def __str__(self):
		msg='当前房间可用面积为：'+str(self.area)+','
		if len(self.containsitem)>0:
			msg=msg+'容纳的物品有：'
			for temp in self.containsitem:
				msg=msg+temp.getname()+','
			msg=msg.strip(',')
		return msg

	def accommodateitem(self,item):
		needarea=item.getusedarea()
		if self.area>needarea:
			self.containsitem.append(item)
			self.area-=needarea
			print('ok,已经存放到房间')
		else:
			print('err:房间可用面积为：%d,但是当前要存放物品所需要的面积为%d'%(self.area,needarea))
		
	def key(self):
		if self.light=='on':
			print('床部分的灯亮了')
			#newbed.key(on)

class bed:
	def __init__(self,area,name='床'):
		self.name=name
		self.area=area
		self.light='on'
		
	def __str__(self):
		msg='床的面积为：'+str(self.area)
		return msg
	
	def getusedarea(self):
		return self.area

	def getname(self):
		return self.name

	def key(self):
		if self.light=='on':
			print('床部分的灯亮了')

newhome=home(100)
print(newhome)

newbed=bed(20)
print(newbed)

newhome.accommodateitem(newbed)
print(newhome)

newbed2=bed(30,'席梦思')
print(newbed2)

newhome.accommodateitem(newbed2)
print(newhome)

newhome.key(on)
