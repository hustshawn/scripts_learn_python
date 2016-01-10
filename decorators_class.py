"""
	The code below demonstrate the functions within a class with the decorators.
"""

class A(object):

	def foo(self, x):
		print "Executing foo(%s, %s)" %(self, x)

	@classmethod
	def class_foo(cls, x):
		print "Executing class_foo(%s, %s)" %(cls, x)

	@staticmethod
	def static_foo(x):
		print "Executing static_foo(%s)" %(x)


a = A()

a.foo(1)
a.class_foo(2)
a.static_foo(3)