"""
TITLE: Dot and Cross

INPUT:
2
1 2
3 4
1 2
3 4

OUTPUT:
[[ 7 10]
 [15 22]]

"""
import numpy as np

n = int(input())
my_array_1 = np.array([input().strip().split() for _ in range(n)], int)
my_array_2 = np.array([input().strip().split() for _ in range(n)], int)
print(np.dot(my_array_1, my_array_2))
