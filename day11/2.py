class f1:
	def __init__(self):
		self.cookedlevel=0
		self.cookedstring='生的'
		self.condiments=[]

	def __str__(self):
		msg=self.cookedstring+'地瓜'
		if len(self.condiments)>0:
			msg=msg+'('
			for temp in self.condiments:
				msg=msg+temp+','
			msg=msg.strip(',')
			msg=msg+')'
		return msg
	
	def cook(self,time):
		self.cookedlevel+=time
		if self.cookedlevel<=3:
			self.cookedstring='生的'
		elif self.cookedlevel<=5:
			self.cookedstring='半生'
		elif self.cookedlevel<=8:
			self.cookedstring='烤好啦'
		else :
			self.cookedstring='烤成木炭啦！'
	def addcondiments(self,condiments):
		self.condiments.append(condiments)
myf1=f1()
print('————————还有一个地瓜没有烤——————')
#print(myf1.cookedlevel)
#print(myf1.cookedstring)
#print(myf1.condiments)
print('——————接下来要进行烤地瓜啦——————')
print('————地瓜已经烤了4分钟啦————')
myf1.cook(4)
print(myf1)
print('————地瓜又经烤了3分钟啦————')
myf1.cook(3)
print(myf1)
print('————接下来要添加配料——番茄酱————')
myf1.addcondiments('番茄酱')
print(myf1)
