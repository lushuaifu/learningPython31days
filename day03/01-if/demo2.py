#工资
salary = int(input('输入工资：'))
#计算基数
num = salary-3500
#税率
rate = 0

'''
if salary>0:
	print('收税')
	if salary<=1500
		rate = 0.03
	else:
		if salary<=4500
			rate = 0.1
		else
			.....
			
else:
	print('不收税')
'''
if num>0:
	print('收税')
	if num<=1500:
		rate = 0.03
	elif num<=4500:
		rate = 0.1
	elif num<=9000:
		rate = 0.2 
	elif num<=35000:
		rate = 0.25
	elif num<=55000:
		rate = 0.3
	elif num<=80000:
		rate = 0.35
	else:
		rate = 0.45

	#计算税
	tax = num*rate
	print('工资是%d,税率是%0.2f,税是%f'%(salary,rate,tax))
else:
	print('不收税')




'''
	写代码的方法：
	1、输入并获取薪水，-3500
	2、判断
		1、如果>0收税，否则不收税
		2、收税再细分
			1、如果1500以下 0.03
			2、如果1500以上，4500以下，0.1
			。。。。

		if 薪资-3500>0:
			if 1500以上：
				xx
			elif 4500以下
				xx
			elif ,,,,,,,
		else:
			不收税
'''

