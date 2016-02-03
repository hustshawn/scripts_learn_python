vec = [2 , 4, 6]
vec2 = [3*x for x in vec]
print(vec2)

import sys
print("py3")
print(sys.version)


params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

b = ["%s=%s" % (k, v) for k, v in params.items()]
print(b)

import calendar

monthRange = calendar.monthrange(2015,12)
print(monthRange)


import math
print(math.log10(1000))

