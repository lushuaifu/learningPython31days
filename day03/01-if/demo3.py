'''
	根据分数划分等级
	0-100

	0-60		D
	60-80		C
	80-90		B
	90-100		A

	1、输入获取分数
		1、str--->int  因为要与数字进行比较
		2、判断0-100之间
	2、判断等级
		连续的判断范围 if elif .... else
'''

score = int(input('输入分数：'))
if score>=0 and score<=100:
	if score<60:
		print('D')
	elif score<80:
		print('C')
	elif score<90:
		print('B')
	else:
		print('A')
else:
	print('请输入0-100之间的数字')