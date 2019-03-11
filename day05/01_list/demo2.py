#定义list
nums=[1,2,3,3,3,5656,3]
num = 3
'''
	删除的方法：remove
	删除之前判断的方法：in
	查询有几个值：count

	循环 while
'''
print(nums)
while num in nums:
	nums.remove(num)
print(nums)
