nums = [0,1,2,3,4,5,6,7,8,9]

#while遍历
m=0
n=len(nums)
while m<n:
	print(nums[m])
	m+=1

#for遍历
'''
	m=0
	n=len(nums)
	while True:
		if(m>=n):
			break
		temp=nums[m]
		m+=1
'''

for temp in nums:
	print(temp)

