a = [0, 1, 2, 3, 4, 5, 6, 7]
b = map(lambda x:x+3, a)
b_list = list(b)
print(b)
print(b_list)


a = [1, 2, 3]
b = [4, 5, 6]
# map two sequence
print(list(map(lambda x,y:x+y, a, b)))


# To implement a map function
def my_map(func, *args):
	return [ func(arg) for arg in args ]
	