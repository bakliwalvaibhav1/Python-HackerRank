"""
TITLE: itertools.product()

INPUT:
1 2
3 4

OUTPUT:
(1, 3) (1, 4) (2, 3) (2, 4)

"""

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))
