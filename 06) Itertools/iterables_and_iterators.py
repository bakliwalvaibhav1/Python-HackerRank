"""
TITLE: Iterables and Iterators

INPUT:
4
a a c d
2

OUTPUT:
0.833

"""

import itertools

N = int(input())
mylist = input().split()
K = int(input())

elementsWithA = 0

op = list(itertools.combinations(mylist, K))
for i in op:
    if 'a' in i:
        elementsWithA += 1

print(round(elementsWithA/len(op), 3))
