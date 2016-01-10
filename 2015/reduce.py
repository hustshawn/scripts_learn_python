# Python 3 reuqired
from functools import reduce

""" 
To understand "reduce" function
reduce(f, [x1, x2, x3, x4]) = f ( f ( f ( x1, x2 ), x3 ), x4 )
Each time accept a new argument with the existing result , 
which composed as a pair of arguments
"""

def fn(x,y):
	return x * 10 + y

r = reduce(fn, [1, 3, 5, 7, 9])
print(r)


# def str2int(s):
# 	return reduce(lambda x,y: x*10+y, map(int,s))

# text = "abc"
# print(str2int(text))
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int("13579"))

# Normalize the string, first char uppercase
def normalize(s):
	return s[0].upper() + s[1:].lower()
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Product a list items
def prod(L):
	return reduce(lambda x, y: x * y, L)

print(prod([1,2,3,4,5]))




# def str2float(s):
# 	dot_index = s.index(".")
# 	s = s.split('.')
# 	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# print(str2float("12.34"))

s = "123.45"
times = len(s) - s.index(".") - 1
s = s.replace(".","")
print(str2int(s) * (0.1 ** times))


s = "123323.456789"
s_split = s.split(".")
dec = s_split[0]
frac = s_split[1]
print(str2int(dec) + 0.1 * reduce(lambda x, y: x *0.1 + y , list(map(char2num, frac))[::-1]))

s_new = "123323.456789"
def prod(s):
	s_split = s.split(".")
	dec = s_split[0]
	frac = s_split[1]
	return str2int(dec) + 0.1 * reduce(lambda x, y: x *0.1 + y , list(map(char2num, frac))[::-1])

print(prod(s_new))
