"""
TITLE: Polynomials

INPUT:
1.1 2 3
0

OUTPUT:
3.0

"""
import numpy as np

n = list(map(float, input().split()))
m = input()
print(np.polyval(n, int(m)))
