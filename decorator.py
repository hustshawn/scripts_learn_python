# def log(func):
# 	def wrapper(*args, **kw):
# 		print("call %s():", % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	"""
	which equals now = log(now)
	"""
	print('2015-06-15')


# log(now)

now()
print(now.__name__)