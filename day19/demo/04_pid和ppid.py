import os

'''
    fork主进程结束，表示程序结束。
    通过判断既可以操作父进程，又可以操作子进程
'''

pid = os.fork()
if pid == 0:
    print('haha...pid=%s,ppid=%s'%(os.getpid(),os.getppid()))
else:
    print('哈哈...pid=%s,ppid=%s' % (os.getpid(), os.getppid()))
'''
    哈哈...pid=2753,ppid=2369
    haha...pid=2754,ppid=2753
'''

'''
fork炸弹
while True:
    os.fork()
'''
