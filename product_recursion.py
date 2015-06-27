
def product(x, y):
	if x == 0 or y == 0:
		return 0
	elif y == 1:
		return x
	else:
		return product(x, y-1) + x

# To test the product()
print(product(20, 6))