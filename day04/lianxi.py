num=['唐三藏','孙悟空','猪八戒','沙悟净']
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[-1])
print(num[-2])
print(num[-3])
print(num[-4])
print()

num=['唐三藏','孙悟空','猪八戒','沙悟净']
tax=0
while tax<len(num):
    print(num[tax])
    tax+=1
print()

num2=[123,3.14,'旺财',None,True,num]
tax2=0
while tax2<len(num2):
    print(num2[tax2])
    tax2+=1
print()

num2=[123,3.14,'旺财',None,True,num[0]]
tax2=0
while tax2<len(num2):
    print(num2[tax2])
    tax2+=1
print()

num2=[123,3.14,'旺财',None,True,num[1:3]]
tax2=0
while tax2<len(num2):
    print(num2[tax2])
    tax2+=1
print()
