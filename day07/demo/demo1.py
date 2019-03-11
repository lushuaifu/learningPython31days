'''
	定义语法：
	def 函数名():
		语句块
'''
print('begin......')
#定义
def funOne():
	i=0
	while i<10:
		print('好好学习，天天向上。%s'%i)
		i+=1
#调用
funOne()
print('over......')