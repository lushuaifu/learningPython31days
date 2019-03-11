nums1=[1,2,3]
nums2=[3,4,5]
nums3 = nums1+nums2
print(nums1,nums2,nums3)

nums4 = nums1*4

print(nums1,nums4)

nums1=[1,20,3]
nums1.sort()
print(nums1)

#遍历/迭代list==循环list里的所有的值

nums1=[1,20,3]
#循序反过来
nums1.reverse()
print(nums1)

'''
nums1=[1,20,3]
i = 0
length = len(nums1)
while i<length:
	print(nums1[i])
	i+=1
'''
'''
nums1=[1,20,3]
length = len(nums1)
i = length-1 
while i>=0:
	print(nums1[i])
	i-=1
'''
'''
nums1=[1,20,3]
i = -1
length = len(nums1)
while i>=-length:
	print(nums1[i])
	i-=1
'''
nums1=[1,20,3]
nums2=[]
# 变量名 = 长度
length = len(nums1)
i = length-1 
while i>=0:
	print(nums1[i])
	nums2.append(nums1[i])
	i-=1
nums1 = nums2
print(nums1,nums2)



'''
	1、根据老师的材料，能整出来
	2、抛开老师的资料，自己写
		1、用汉字进行分析步骤
		2、改代码
		3、不懂-->看老师的资料-->再写


	问题l：循环显示的内容

	1、定义list
	2、使用while
		1、条件
			定义一个变量，每次加1,判断不能越界
		2、循环体
			根据变量，获取每一个值，改变下标

	时间 == 好的结果   false   -->提高效率
'''
