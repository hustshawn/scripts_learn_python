a = [1, 2, 3, 4, 5, 6, 7]
b = filter(lambda x:x>2, a)
# print(b.items())
b_list = list(b)
print(b_list)

# Or just iter with "in" operator
# for i in b:
# 	print(i)
c = (i for i in a if i % 2 != 0)
c_list = list(c)
print(c)
print(c_list)