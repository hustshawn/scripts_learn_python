# Implement with generator
# def fib(max):
# 	b, i, a = 1, 0, 0

# 	while i < max:
# 		yield b;
# 		b , a = b + a, b
# 		i += 1

# for i in fib(2):
# 	print(i)


def trace(f):
    f.indent = 0
    def g(x):
        print('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        value = f(x)
        print('|  ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g


#Implement fibonacci with recursion

@trace
def fib(n):
	if n is 0 or n is 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(4))
