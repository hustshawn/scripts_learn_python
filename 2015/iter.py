import itertools

x = [1, 2, 3]
y = ['A', 'B', 'C']
z = ['a', 'b', 'c']

# Iter chain 
it1 = iter([1,2,3])
it2 = iter([4,5,6])
it3 = itertools.chain(it1, it2)
for i in it3:
	print(i)

print(it3)

# Zip as a iter
it4 = iter(zip(x,y,z))
for a,b,c in it4:
	print(a,b,c)
