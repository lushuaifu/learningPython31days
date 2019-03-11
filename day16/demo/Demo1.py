ls1 = list(range(10))
print(ls1)
print(type(ls1))
#列表生成器
ls2 = [x for x in range(10) if x%2==0]
print(ls2)
print(type(ls2))



'''
range:python2和python3的区别
'''
ret = range(1000000000000000000000)
for i in ret:
    print(i)

