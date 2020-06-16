"""
TITLE: Inner and Outer

INPUT:
0 1
2 3

OUTPUT:
3
[[0 0]
 [2 3]]

"""
import numpy as np

my_array_1 = np.array([input().strip().split()], int)
my_array_2 = np.array([input().strip().split()], int)

print(int(np.inner(my_array_1, my_array_2)))
print(np.outer(my_array_1, my_array_2))


