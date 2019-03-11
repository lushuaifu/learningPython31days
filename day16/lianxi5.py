import time
def test1():
    while 1:
        print('--1--')
        yield None
def test2():
    while 1:
        print('--2--')
        yield None
t1=test1()
t2=test2()
while 1:
    time.sleep(1)
    t1.__next__()
    t2.__next__()
