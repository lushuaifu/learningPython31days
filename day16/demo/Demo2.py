'''
generator:生成器
相当于保存了一个算法，使用的时候
'''
ge = (x for x in range(10))
print(ge)
print(type(ge))

num = next(ge)
print(num)
num = next(ge)
print(num)

print('*'*20)

for num in ge:
    print(num)
