print('你好，python')
f=open('1.txt','w')
f.write('abc\n')
f.write('123\n')
f.write('中文\n')
f.close()

f=open('test.txt','r')
s0=f.read(1)
num1=f.tell()
s1=f.read()
num2=f.tell()
s2=f.read()
num3=f.tell()
print(s0,s1,s2,num1,num2,num3)


f=open('test.txt','r')
lines=f.readlines()
print(lines)
for line in lines:
	print(line)

f=open('test.txt','r')
while 1:	
	line=f.readline()
	if line=='':
		break
	print(line)

