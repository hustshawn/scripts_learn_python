import timeit

bad_chars = '(){}<>'

setup = """import re
import string
s = 'Barack (of Washington)'
bad_chars = '(){}<>'
rgx = re.compile('[%s]' % bad_chars)"""

timer = timeit.Timer('o = "".join(c for c in s if c not in bad_chars)', setup=setup)
print "List comprehension: ",  timer.timeit(100000)


timer = timeit.Timer("o= rgx.sub('', s)", setup=setup)
print "Regular expression: ", timer.timeit(100000)

timer = timeit.Timer('for c in bad_chars: s = s.replace(c, "")', setup=setup)
print "Replace in loop: ", timer.timeit(100000)

timer = timeit.Timer('s.translate(string.maketrans("", "", ), bad_chars)', setup=setup)
print "string.translate: ", timer.timeit(100000)