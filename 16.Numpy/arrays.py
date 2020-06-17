"""
TITLE: ARRAYS

INPUT:
1 2 3 4 5 7

OUTPUT:
[7. 5. 4. 3. 2. 1.]

"""
import numpy


def arrays(arr):
    myarr = numpy.array(arr, numpy.float32)
    myarr = myarr[::-1]
    return myarr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
