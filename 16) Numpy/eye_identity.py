"""
TITLE: Eye and Identity

INPUT:
3 3

OUTPUT:
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""
import numpy

print(str(numpy.eye(*map(int, input().split()))).replace('1', ' 1').replace('0', ' 0'))
