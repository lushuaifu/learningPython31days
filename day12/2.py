class base:
	
	def test(self):
		print('--base test--')

class A(base):
	pass
'''
	def test(self):
		print('--A test--')
'''
class B(base):
	def test(self):
		print('--B test__')
class C(A,B):
	pass

obj_C=C()
obj_C.test()
print(C.__mro__)
