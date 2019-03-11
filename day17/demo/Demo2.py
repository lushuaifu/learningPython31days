'''


'''
def outer(fn):
    print('outer......')
    def inner():
        print('相亲准备前.....查看照片好看不，xxxxxx')
        #if True:
        #try
        fn()
        #except:
        print('相亲准备后.....')
    return inner

@outer
def miai():
    print('相亲中......')


miai()


