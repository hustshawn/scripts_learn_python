# To divide a num to list
def num2list(n):
	L = []
	while n > 0:
		L.append(n % 10)
		n = int(n / 10)
	return L

# To decide whether the number is palindrome
def is_palindrome(n):
	num_list = num2list(n)
	# cmp_list = num2list(n)[::-1]
	cmp_list = num_list[::-1]
	if num_list == cmp_list:
		return n

# Output test
print(is_palindrome(121))
output = filter(is_palindrome, range(1000))
print(list(output))