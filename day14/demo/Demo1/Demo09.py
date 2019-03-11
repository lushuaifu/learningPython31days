
try:
    print('-----test--1---')
    f = open('123.txt', 'a')
    f.write('写啥都行。。。。')
    #num = 1/0
    print('-----test--2---')
except Exception:
    print('except...')
finally:
    print('finally...')
    f.close()
print('over...')
print(f.closed)
