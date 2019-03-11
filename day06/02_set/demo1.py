#定义set
s1 = {2,3,4,1434}
print(s1)
#新增，如果存在，新增不进去
s1.add(22)
print(s1)
#移除，如果不存在，报错keyerror
s1.remove(2)
print(s1)
print(3 in s1)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = {4,5,6,7}

print(s1|s2)
print(s1&s2)
print(s1-s2,s1)
#更新
s1.update(s2,s3)
print(s1)


s1 = {1,2,3}
s2 = {3,4,5}
s1.discard(2)
print(s1)

s1 = {14,21111,3,'a',1}
print(s1.pop(),s1)

ret = {1,2,3,4}.issubset({1,2,3})
print(ret)

ret = {1,2,3,4}.issuperset({1,2,3})
print(ret)

ls = [1,2,3,1,234,1111,333455]
#去重复
s = set(ls)
print(s)

