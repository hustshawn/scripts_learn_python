def flatten_dict(a, result=None, key=None):
	"""
		>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
	"""
	if result is None:
		result = {}

	for k, v in a.items():
		if isinstance(v, dict):
			flatten_dict(v, result, k)
		else:
			if key:
				result[key+'.'+k] = v
			else:
				result[k] = v
	return result

# To test the functionality
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))


# k = "abc.12345"
# k_split = k.split('.')
# out_key = k_split[0]
# in_key = k_split[1]

# print(k_split)
# print(type(out_key))# print(in_key)

# l = {'a':1, 'b':2}
# if l['c'] is '':
# 	print("work")

# else:
# 	print("not work")

def unflatten_dict(a, result=None):
	"""
	>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
	{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
	"""
	if result is None:
		result = {}

	for k, v in a.items():
		if '.' in k:
			k_split = k.split('.')
			out_key, in_key = k_split[0], k_split[1]
			try:
				result[out_key]
			except KeyError:
				result[out_key] = {in_key: v}
			else:
				result[out_key][in_key] = v
		else:
			result[k] = v

	return result

# Output verify
print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4, 'd.z':5}))


