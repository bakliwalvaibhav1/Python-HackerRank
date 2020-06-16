"""
TITLE: Array Mathematics

INPUT:
1 4
1 2 3 4
5 6 7 8

OUTPUT:
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]

"""
import numpy

N,M=map(int,input().split())

A=numpy.array([list(map(int,input().split())) for n in range(N)])
B=numpy.array([list(map(int,input().split())) for n in range(N)])

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
m=A/B

print(numpy.int_(m))

print(numpy.mod(A,B))
print(numpy.power(A,B))
