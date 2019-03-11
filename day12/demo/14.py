''' 
类属性 
    1、每个对象都有这个属性
    2、如果通过 类修改的，所有的都会被修改
    3、如果通过 对象修改的，只会修改当前这一个对象的，其它并不受影响



实例属性
'''

class Student:
    #类属性
    kongtiao = 1


wangcai = Student()
print(wangcai.kongtiao)
xiaoqiang = Student()
print(xiaoqiang.kongtiao)


print('-'*20)
wangcai.kongtiao = 110
print(wangcai.kongtiao)
print(xiaoqiang.kongtiao)
print(Student.kongtiao)



'''
print('-'*20)
Student.kongtiao = 2
print(wangcai.kongtiao)
print(xiaoqiang.kongtiao)
print(Student.kongtiao)
'''
