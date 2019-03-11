num=[0,1,2,3,4,5,6,7,8]
n=0
while n<len(num):
    print(num[n])
    n+=1
    
print()


for temp in num:
    print(temp)


a=10
b=10
print(a,id(a),b,id(b))
print()


a=[1,2,3]
b=[1,2,3]
print(a,id(a),b,id(b))
print()

a=[1,2,3]
b=a
b[0]=110
print(a,id(a),b,id(b))
print()


a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
