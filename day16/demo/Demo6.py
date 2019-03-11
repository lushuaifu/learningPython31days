import  time

def test1():
    while True:
        print("--1--")
        yield None

def test2():
    while True:
        print("--2--")
        yield None


t1 = test1()
t2 = test2()
print(t1)
print(t2)

print('*'*100)

while True:
    #time.sleep(0.1)
    t1.__next__()
    t2.__next__()

