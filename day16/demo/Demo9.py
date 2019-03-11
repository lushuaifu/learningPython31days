def outer(num):
    print('outer...')
    def inner():
        print('inner...')
        print(num)
    return inner


ret = outer(100)
#ret()
#print(outer)