# A generator to generate an odd number sequence
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# Light weight func to determine division or not
def _not_divisible(n):
    return lambda x: x % n > 0

def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # it = filter(_not_divisible(n), it)
        it = filter(lambda x: x % n > 0, it)
        # 可见通过filter函数，可以将条件应用到整个generator当中，即便有些元素尚未生成.


# Output Test
for n in prime():
    if n < 18:
        print(n)
    else:
        break