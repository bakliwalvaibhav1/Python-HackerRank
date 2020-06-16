"""
TITLE: Mean, Var and Std

INPUT:
2 2
1 2
3 4

OUTPUT:
[ 1.5  3.5]
[ 1.  1.]
1.11803398875

"""
import numpy as np

np.set_printoptions(sign=' ')
n, m = map(int, input().split())
my_array = np.array([input().strip().split() for _ in range(n)], int)

print (np.mean(my_array, axis = 1))
print (np.var(my_array, axis = 0))
print (round(np.std(my_array), 12))
