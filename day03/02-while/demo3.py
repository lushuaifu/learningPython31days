'''
打印九九乘法表

次   算式
1		1
2		2
3		3
n		n
'''

'''
n*m 
n<=m
m = 1
n = 1
while m<10:
	m+=1
	while n<m+1:
		n+=1
		print(m,n)
'''
'''
print('哈哈',end='')
print('呵呵')
print('嘿嘿')

print('%s %s'%('呵呵','哈哈'))
'''

'''
\t制表位tab
\n换行
'''
m = 1
n = 1
while m<10:
	while n<m+1:
		print('%d*%d=%d'%(n,m,m*n),end='\t')
		n+=1
	print('')
	n=1
	m+=1