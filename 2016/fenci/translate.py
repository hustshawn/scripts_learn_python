a = "this isn't a word, right."
tt = str.maketrans("'.?", "   ")
result = a.translate(tt)
print(result)
# this isn t a word, right