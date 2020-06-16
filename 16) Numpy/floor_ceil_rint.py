"""
TITLE: Floor Ceil and Rint

INPUT:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

OUTPUT:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
import numpy

numpy.set_printoptions(sign=' ')
my_array = numpy.array(list(map(float, input().split())))
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))
