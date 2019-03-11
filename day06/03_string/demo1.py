name = 'python雍老师'
#通过下标获取
print(name[7])
#遍历循环
for temp in name:
	print(temp)
#格式化
name = '旺财'
age = 10
score = 59.991

ret = '姓名是：%s,年龄是：%d,分数：%0.2f'%(name,age,score) 
print(ret)

print('亲爱的xx:\n\t好久不见，甚是\'想念\'。\\')