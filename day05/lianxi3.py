nums=('水浒传','西游记','红楼梦','三国演义','123')
#列表增删改都不能用，只能查询
index=nums.index('123')
print(index)
print(len(nums),type(nums))

t1=[1,2,3]
t2=(t1,110)
print(t2)
print(t2[0][1])
t2[0][1]=99
print(t2)


ls=[1,2,3]
t=tuple(ls)
print(ls,t)

t=(4,5,6)
ls=list(t)
print(t,ls)
