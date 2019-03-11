import time
'''
num = 1;
while num<10:
	num+=1
	if num==8:
		break
		#continue
	print(num)
'''
'''
while True:
	print('outer.......')
	while True:
		print('inner.......')
		time.sleep(1)
'''
num = 1
while True:
	time.sleep(0.1)
	print('outer.......')
	while num<10:
		num+=1
		if num==8:
			#break
			continue
		print(num)
		time.sleep(0.1)
print('over...')
	

