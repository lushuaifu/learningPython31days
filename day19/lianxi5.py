import os 
import time
num=0
pid=os.fork()
if pid==0:
	num+=1
	print('哈哈。。。num=%d'%num)
else:
	time.sleep(1)
	num+=1
	print('哈哈2.。。。num=%d'%num)

