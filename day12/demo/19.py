class Student:
    @classmethod
    def haha(cls):
        print('student...haha...%s,%s'%(cls,id(cls)))
    def hehe(self):
        print('stuent...hehe...%s,%s'%(self,id(self)))

s1 = Student()
#s1.haha()

s1.hehe()
Student.haha()


Student.hehe(s1)


