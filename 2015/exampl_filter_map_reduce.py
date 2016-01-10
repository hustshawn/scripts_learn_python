x = [{'a':1, 'b':2}, {'c':3}, {'d':4}]
y = [{'a':1}, {'c':3},{'e':5}]

f = filter(lambda z: (x+y).count(z)<2, (x+y))
print(list(f))


#flatten out nested sublist
#result: [ 1, 2, 3, 4, 5 ]
import operator
from functools import reduce
r = reduce( operator.concat, [ [ 1, 2 ], [ 3, 4 ],[ 5 ] ], [ ] )
print(list(r))

for i in range(0,10):
	print(i)

# 一行并发
import urllib2  
from multiprocessing.dummy import Pool as ThreadPool

urls = [  
           'http://www.python.org',
           'http://www.google.com',
           'http://www.baidu.com',
           'http://www.python.org/community/',
           'http://www.saltstack.com'
           ]

#pool = ThreadPool()
pool = ThreadPool(4) # Sets the pool size to 4

result = pool.map(urllib2.urlopen, urls)  
pool.close()  
pool.join()  