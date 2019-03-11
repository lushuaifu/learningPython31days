#建议键一般使用字符串
dogs={'1':'旺财','2':'小强','3':'阿黄'}
print(dogs)
#通过键获取值
print(dogs['1'])
#新增，如果键已经存在，覆盖原来的
dogs['4']='叮当'
dogs['1']='叮当当'
print(dogs)
#删除
dogs={'1':'旺财','2':'小强','3':'阿黄'}
v1=dogs.pop('1')
print(v1)
print(dogs)

dogs={'1':'旺财','2':'小强','3':'阿黄'}
del dogs['1']
print(dogs)

dogs={'1':'旺财','2':'小强','3':'阿黄'}
dogs.clear()
print(dogs)

dogs={'001':'旺财','002':'小强','003':'阿黄'}
#get获取，如果获取不到，结果是None，可以设置默认值
print(dogs.get('001'))
print(dogs.get('0011'))
print(dogs.get('0011','未知'))
print(dogs.get('001','未知'))

#获取键值对的个数
num=len(dogs)
print(num)

#转字符串
s=str(dogs)
print(type(s),s)

#获取所有的key
keys=dogs.keys()
print(keys)

for i in keys:
    print(i)
print(type(keys))

#获取所有的value
values = dogs.values()
print(values)

for i in values:
    print(i)
print(type(values))

#获取所有的key values对
kws=dogs.items()
print(kws)

for i in kws:
    #print(i,type(i))
    print('%s=%s'%(i[0],i[1]))
print(type(kws))
