"""
TITLE: Linear Algebra

INPUT:
2
1.1 1.1
1.1 1.1

OUTPUT:
0.0

"""
import numpy as np

n = int(input())
my_array = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(my_array), 2))
