'''


'''
def outer(fn):
    print('outer......')
    def inner():
        print('inner....')
        fn()
    return inner

@outer              #myFunc = outer(myFunc)
def myFunc():
    print('myFunc......')

myFunc()
#myFunc = outer(myFunc)
#myFunc()


#print(myFunc)
myFunc()


