from abc import ABCMeta, abstractmethod

class Shape(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass


class Rectangle(Shape):

	def __init__(self, width, hight):

		self.width = width
		self.hight = hight
		
		super(Rectangle, self).__init__()

	def area(self):
		return self.width * self.hight

	def perimeter(self):
		return (self.width + self.hight) * 2

class Square(Rectangle):

	def __init__(self, line_length):
		
		self.line_length = line_length
		super(Square, self).__init__(line_length, line_length)

	def area(self):	
		return self.line_length * self.line_length

	def perimeter(self):
		return self.line_length * 4


sq = Square(5)

print(sq.area())


