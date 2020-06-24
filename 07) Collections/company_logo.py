"""
TITLE: Company Logo

INPUT:
aabbbccde

OUTPUT:
b 3
a 2
c 2

"""


from collections import Counter

class OrderedCounter(Counter):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]