import os
import time

num = 0

# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
pid = os.fork()

if pid == 0:
    num+=1
    print('哈哈1---num=%d'%num)
else:
    time.sleep(1)
    num+=1
    print('哈哈2---num=%d'%num)
