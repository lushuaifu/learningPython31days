'''
	python是一个弱类型语言，java是一个强类型语言
'''
a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(10/3)
print(a//b)
print(b//a)
print(10//3)
print(a%b)

print('-'*10)

print(a>b)
print(a!=b)
print(a==b)

print('-'*10)

num = 10
#num = num+20
num+=20
#java,c#   num++--
num+=1
num//=4
print(num)

print('-'*10)


print(bin(60),bin(13))
'''
	0b111100 
	0b001101
	0b001100
'''
num = 60&13
print(num)
print(int('0b001100',2))

'''
	左移:相当于乘以2的n次方
	右移:相当于除以2的n次方
'''
print(60<<2)
print(60>>2)


print('-'*10)

print(True and False)
print(True or False)
print(10 and 20)
print(False and 20)
print('' and 20)
print(' ' and 20)
print(None and 20)
print(0 and 20)
print(-100 and 20)

print(10 or 20)
print(False or 20)
print('' or 20)
print(' ' or 20)
print(None or 20)
print(0 or 20)
print(-100 or 20)

print(not False)
print(not 10)

print('-'*10)
print('a' in 'china')
print('a' not in 'china')

print('-'*10)
num1 = 10000000000
num2 = 10000000000
print(id(num1),id(num2),num1==num2)
print(num1 is num2)

num1 = [20,35,10]
num2 = [20,35,10]
print(id(num1),id(num2),num1==num2)
print(num1 is num2)

ret = (10+20)/2
ret = 4/2
print(ret,type(ret))
