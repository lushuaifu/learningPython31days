class cat:
	def __init__(self,name):
		self.name=name
		self.color='yellow'

class bosi(cat):
	def __init__(self,name):
		#cat.__init__(self,name)
		super().__init__(name)

	def getname(self):
		return self.name

bs=bosi('肥波')
print(bs.name)
print(bs.color)
