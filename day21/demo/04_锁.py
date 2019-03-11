import threading

myLock = threading.Lock()
print(myLock)
print('1...')
#锁住，如果此锁，已经锁了，如果再锁，会阻塞，直到开锁了，才能再锁
myLock.acquire()
print('2...')
#开锁，如果锁住了，可以开锁。如果没锁，直接开，报错
myLock.release()
print('3...')
myLock.acquire()
print('4...')