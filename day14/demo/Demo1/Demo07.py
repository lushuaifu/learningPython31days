
try:
    print('-----test--1---')
    f = open('123.txt', 'a')
    f.write('写啥都行。。。。')

    num = 1/0

    f.close()
    print('-----test--2---')
except Exception:
    print('except...')
    f.close()
print('over...')
