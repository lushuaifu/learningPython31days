class A:
    def test(self,item):
        item.num = 10

class B:
    def __init__(self):
        self.num = 100

a = A()
b = B()

print(b.num)
a.test(b)
print(b.num)
