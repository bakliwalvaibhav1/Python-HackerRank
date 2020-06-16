"""
TITLE: Sum and Prod

INPUT:
2 2
1 2
3 4

OUTPUT:
24

"""

import numpy as np

n, m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)

my_array_2 = np.sum(my_array, axis=0)
print(np.prod(my_array_2))
