"""
TITLE: Zeroes and Ones

INPUT:
3 3 3

OUTPUT:
[[[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

"""
import numpy as np

N = tuple(map(int, input().split()))

print(np.zeros(N, dtype=np.int))
print(np.ones(N, dtype=np.int))
