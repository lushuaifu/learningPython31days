num=['123','456','孙悟空','猪八戒','沙悟净']
num.append('唐三藏')
print(num)
num.insert(1,'大鹏鸟')
print(num)
num.insert(30,'前')
print(num)
num.insert(-2,'后')
print(num)
num.extend(['大','小','多'])
print(num)

print(num[1])
num2=['123','456','孙悟空',[564,897,'我们'],'猪八戒','沙悟净']
print(num2[3][1])
num2[2]='唐三藏'
print(num2)

num3=num2.pop()
print(num3)

num4=num2.pop(3)
print(num4)

num2=['123','456','孙悟空',[564,897,'我们'],'猪八戒','沙悟净','123']
del num2[2]
print(num2)
num2.remove('123')
print(num2)

num3=['123','456','孙悟空',[564,897,'我们'],'猪八戒','沙悟净','123']
lenth=len(num3)
i=0
while i<lenth:
    ret=num3[i]
    i+=1
    if ret=='123':
        num3.remove('123')
print(num3)


