INPUT_NUMBER = 153

number = int(INPUT_NUMBER)

total = 0
n = len(str(number))

num = number
while num > 0:
	digit = num % 10
	total += digit ** n
	# Completely divide '//'
	num //= 10
print("Total:",total)
if number == total:
	print(number, " is Armstrong number")
else:
	print(number, " is not Armstrong number")


