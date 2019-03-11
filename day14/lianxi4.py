try:
    print('----test--1---')
    open('123.txt','r')
    print('----test--2---')
    print(num)
except(IOError,NameError) as result:
    print(result)