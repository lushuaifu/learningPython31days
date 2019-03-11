class Student:
    name = '哈哈'



s1 = Student()
print(s1.name)


s1.name = 'xx'

del s1.name

print(Student.name)
print(s1.name)
