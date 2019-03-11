'''
函数的嵌套

'''
'''
def f1():
	print('f1...begin')
	f2()
	print('f1...end')

def f2():
	print('f2...begin')
	print('f2...end')

f1()
'''

def f1(a):
	print('f1...begin')
	f2(a,a+1)
	print('f1...end')

def f2(a,b):
	print('f2...begin')
	print(a,b)
	print('f2...end')

f1(110)

nums=[1,2,3]
def f1(nums):
	nums.append('a')

print(nums)
f1(nums)
print(nums)


