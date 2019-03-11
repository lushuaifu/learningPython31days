names = ('西游记','水浒传','三国演义','红楼梦')
#tuple定义好之后，不能修改
#names[0] = '人民的名义'
print(names[1])
print(names,type(names))

nums=()
print(len(nums))

#如果只有一个值，需要在后面加,
nums=('a',)
print(len(nums),type(nums))
#列表的增删改都不能用，只能查询
index = nums.index('a')
print(index)


t1 = [1,2,3]
t2 = (t1,110)
print(t2[0][2])

t2[0][2] = 99

print(t2)


ls = [1,2,3]
t = tuple(ls)
print(ls,t)

t = (1,2,3)
ls = list(t)
print(t,ls)




