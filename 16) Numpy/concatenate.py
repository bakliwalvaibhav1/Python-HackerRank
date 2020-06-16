"""
TITLE: Concatenate

INPUT:
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4

OUTPUT:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]

"""

import numpy as np

n, m, p = map(int, input().split())
array_1 = np.array([input().strip().split() for _ in range(n)], int)
array_2 = np.array([input().strip().split() for _ in range(m)], int)
print(np.concatenate((array_1, array_2), axis=0))
