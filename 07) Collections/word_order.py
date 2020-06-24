"""
TITLE: Word Order

INPUT:
4
bcdef
abcdefg
bcde
bcdef

OUTPUT:
3
2 1 1

"""

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
