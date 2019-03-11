
class people(object):
	def __init__(self,name):
		self.__name=name

	def getname(self):
		return self.__name

	def setname(self,newname):
		if len(newname)>=5:
			self.__name=newname
		else:
			print('error:名字长度需要大于5')
xiaoming=people('xx')
xiaoming.setname('yy')
print(xiaoming.getname())
xiaoming.setname('lishi')
print(xiaoming.getname())

