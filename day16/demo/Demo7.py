import  collections

for i in [1,2,3]:
    print(i)
for i in (1,2,3):
    print(i)
for i in 'abc':
    print(i)
for i in {'id':1,'age':2}:
    print(i)

print(isinstance([],collections.Iterable))
print(isinstance([],collections.Iterator))
#生成器一定可以迭代,而且是迭代器
print(isinstance((x for x in range(10)),collections.Iterable))
print(isinstance((x for x in range(10)),collections.Iterator))


ls1 = [1,2,3,4]
ls2 = [1,2,3,4]

iter1 = iter(ls1)
print(ls1)
print(iter1)
print(isinstance(ls1,collections.Iterator))
print(isinstance(iter1,collections.Iterator))
#print(next(iter1))
for i in iter1:
    print(i)