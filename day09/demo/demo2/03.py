#coding:utf-8
f = open('t.txt','r')
#读指定个数的字符，这里读了一个，光标往下移动了一个
s0 = f.read(1)
#光标的位置
num1 = f.tell()
#从光标这读到末尾
s1 = f.read()
num2 = f.tell()
#如果已经到末尾了，再读返回''
s2 = f.read()
num3 = f.tell()
print(s0,s1,s2,num1,num2,num3)
