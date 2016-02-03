### A demo to the decorators usage

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



