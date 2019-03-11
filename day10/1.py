class car:
	def f1(self):
		print('汽车在奔跑。。。')
	def f2(self):
		print('车轮个数：%s,颜色：%s'%(self.num,self.color))
baoma=car()
baoma.f1()
baoma.color='red'
baoma.num=4
baoma.f2()

qq=car()
qq.f1()
qq.color='green'
qq.num=6
qq.f2()
