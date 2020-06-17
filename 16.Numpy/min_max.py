"""
TITLE: Min and Max

INPUT:
4 2
2 5
3 7
1 3
4 0

OUTPUT:
3

"""
import numpy as np

n, m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)
my_array_2 = np.min(my_array, axis=1)
print(np.max(my_array_2))
