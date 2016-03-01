l = [1,2,0, 3, 5]

for i in l:

	try:
		a = 10 / i
	except:
	# 	pass
		print(i, 'caused exception')
		continue
	print(i, '===>', a)