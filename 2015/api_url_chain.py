# To dynamically defines the url of each API
class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__


# Output test
# Output is : /status/user/timeline/list
print(Chain().status.user.timeline.list)