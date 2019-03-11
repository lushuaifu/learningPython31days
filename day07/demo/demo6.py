'''
	可变参数
	参数必须加*，传递过去之后，会组合成元组
'''
def getSum(*nums):
	print(nums,type(nums))
	ret = 0
	for i in nums:
		ret+=i
	return ret

ret = getSum(1,2,-3,4)
print(ret)
#print(getSum(1,2,3,4))
print(getSum())

ls = [2,3,4,5,1]
t = (2,3,4,5,1)
print(getSum(ls[0],ls[1],ls[2],ls[3],ls[4]))

print(getSum(*ls))
print(getSum(*t))


