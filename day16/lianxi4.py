def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1
    return '结束'
f=gen()
print(next(f))
f.send('haha1...')
f.send('haha2...')
print(next(f))
f.send('haha3...')

print('*'*50)

def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1
    return '结束'
f=gen()
print(f.__next__())
f.send('haha1...')
print(f.__next__())
f.send('haha2...')

