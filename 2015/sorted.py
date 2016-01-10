L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)
L4 = sorted(L, key=lambda t: t[1], reverse=True)
print(L2)
print(L3)
print(L4)