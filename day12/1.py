class A:
	def printA(self):
		print('--A--')

class B:
	def printB(self):
		print('--B--')

class C(A,B):
	def printC(self):
		print('--C--')

obj_C=C()
obj_C.printA()
obj_C.printB()
