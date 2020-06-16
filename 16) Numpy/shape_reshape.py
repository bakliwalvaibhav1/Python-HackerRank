"""
TITLE: Shape and Reshape

INPUT:
1 2 3 4 5 6 7 8 9

OUTPUT:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""
import numpy as np


def reshape(arr):
    myarr = np.array(arr, np.int)
    return myarr.reshape(3, 3)


arr = input().strip().split(' ')
result = reshape(arr)
print(result)
