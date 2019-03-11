ls=[1,233,44,40]
ls.sort()
print(ls)


ls=[1,233,44,40]
ls=sorted(ls)
print(ls)
ls=sorted(ls,reverse=True)
print(ls)
ls=sorted(ls,reverse=False)
print(ls)

ls=[['b',3],['c',1],['a',2]]
print(sorted(ls,key=lambda x:x[1]))
print(sorted(ls,key=lambda x:x[1],reverse=True))

students={'101':['b',3],'1000':['c',1],'500':['a',2]}
print(sorted(students))
print(sorted(students.items(),key=lambda x:x[0]))
print(sorted(students.items(),key=lambda x:x[1][1]))


ls=[1,22,55,44,33]
for i in ls:
    print(i)
students={'101':['b',3],'1000':['c',1],'500':['a',2]}
for i in students.items():
    print(i)
