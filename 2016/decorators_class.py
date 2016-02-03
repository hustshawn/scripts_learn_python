### To learn how decorators work
def log(func):
	def wrapper(*args, **kwargs):
		print "call %s(): " % func.__name__
		print "Do something in the wrapper"
		return func(*args, **kwargs)
	return wrapper

@log
def now():
	""" comments"""
	print "2015-04-01"

now()
print "the now() func name is " + now.__name__



def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def func():
	""" comments"""
	print "2015-04-01"

func()
print func.__name__  



class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print s.score
# s.score = 120
# s.score = "abc"


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