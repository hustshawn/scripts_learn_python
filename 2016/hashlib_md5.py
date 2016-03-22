import hashlib
s = """
SRQYkjs4
c2nJ3ryB
aJxlvT9o
ltEYPryl
esfXjo5z
rcRIspbi
sg1paulF
Tneg5UI2
adBnMjVa
le5RC1rV
kASg506T
26geCTly
0FZiPBb0
11neOFKC
6hvn6iZH
"""

def get_digest(seed):
	md5 = hashlib.md5()
	md5.update(seed.encode('utf-8'))
	return md5.hexdigest()

seeds = s.split()
# print(seeds'\n')
print()
for seed in seeds:
	print(seed + ' ==> ' + get_digest(seed))

result = map(get_digest, seeds)
print([r for r in result])
