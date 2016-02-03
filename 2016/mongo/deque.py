from collections import deque

'''
`deque` can be used as a dual-way list.
available methd include `append()` `pop()`,
and `appendleft()`, `popleft()`
'''

q = deque(['a','b', 'c'])
q.append('x')
q.appendleft('y')
print(q)