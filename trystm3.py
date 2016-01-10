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



class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be an integer!')
		if value < 0:
			raise ValueError('width must be an positive value!')
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise ValueError('height must be an integer!')
		if value < 0:
			raise ValueError('height must be an positive value')
		self._height = value

	@property
	def resolution(self):
		return self._height * self._width

s = Screen()
s.width = 1024
s.height = 768

# print s.resolution

assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
# print type(now)

dt = datetime(2015, 4, 19)
# print type(dt)
# datetime.timestamp(dt)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print cday
# print now + timedelta(hours=10)
# print now - timedelta(days=1)
tz_utc = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc)
print dt


