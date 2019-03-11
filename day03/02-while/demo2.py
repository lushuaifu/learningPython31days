import random

while True:
	user = int(input('请选择数字：石头(1)		剪刀(2)		布(3)：'))
	if user<=3 and user>=1:	
		computer = random.randint(1,3)
		if (user==1 and computer==2)or(user==2 and computer==3)or(user==3 and computer==1):
			print('赢了')	
		elif user==computer:
			print('平手')	
		else:
			print('输了')

		if computer==1:
			computer = '石头'
		elif computer==2:
			computer = '剪刀'
		else:
			computer = '布'

		if user==1:
			user = '石头'
		elif user==2:
			user = '剪刀'
		else:
			user = '布'

		print('用户出的是:%s,计算机出的是:%s'%(user,computer))
		ret = input('要不再玩一把？y or n：')
		if ret=='n':
			#退出循环
			break
	else:
		print('只能输入1-3的值')