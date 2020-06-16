"""
TITLE: Transpose and Flatten

INPUT:
2 2
1 2
3 4

OUTPUT:
[[1 3]
 [2 4]]
[1 2 3 4]

"""

import numpy as np


n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())
