a = 1000000
b = a
print(a,b,id(a),id(b))
b = 110
print(a,b,id(a),id(b))

#常数
a = 1000000
b = 1000000

print(a,id(a),b,id(b))



a = [1,2,3]
b = [1,2,3]

print(a,id(a),b,id(b))

a = [1,2,3]
b = a
print(a,id(a),b,id(b))

a = [1,2,3]
b = a
b[0] = 110
print(a,id(a),b,id(b))


a = [1,2,3]
b = [1,2,3]
#比较的是里面的值
print(a==b)
#比较的是地址
print(a is b)