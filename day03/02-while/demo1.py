'''
length = 1000
num = 0
while num<1000:
	print('跑步。。。。。')
	num+=400
print('over...')
'''

'''
num = 0
while num<10:
	num+=1
	print('抄单词%d'%num)
'''
'''
	打印1-100的偶数

num = 1
while num<101:
	num+=1
	if num%2==0:
		print(num)
'''

'''
num = 1
while num<101:
	print(num)
	num+=1
'''

'''
从1累加，达到10000及以上就停止
num = 1
ret = 10000
sum = 0
while True:
	sum+=num
	if(sum>=10000):
		print(num)
		#循环结束
		break
	num+=1
'''

while True:
	ret = input('要继续玩吗?yes or no:')
	if ret=='yes':
		#结束本次循环，进入下次循环
		continue
	else:
		#结束所在的循环
		break;


