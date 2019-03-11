'''
if True:
	print('哈哈。。。。。。')
	print('呵呵。。。。。。')
print('over......')
'''

'''
if False:
	print('哈哈。。。。。。')
	print('呵呵。。。。。。')
print('over......')
'''
'''
money = int(input('请输入余额:'))
if(money>1000):
	print('肯德基')
'''

'''
money = int(input('请输入余额:'))
if money>1000:
	print('肯德基')
else:
	print('馒头')
'''

'''
	找女朋友：
	1、肤白
	2、貌美
	3、大长腿

	同时满足，三个条件 and

	找女朋友：
	女的行，活的也行
	or
'''
skin = '白'
appearance = '美'
leg = 110

'''
if skin=='白' and appearance=='美' and leg>=120:
	print('女神')
else:
	print('女神经')
'''

'''
#and>or,可以用()修改运算顺序
if skin=='白' or appearance=='美' and leg>=120:
	print('女神')
else:
	print('女神经')
'''
#真 or 真 and 假
