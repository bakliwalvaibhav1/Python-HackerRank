"""
TITLE: DefaultDict Tutorial

INPUT:
5 2
a
a
b
a
b
a
b

OUTPUT:
1 2 4
3 5

"""

from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(*d[input()] or [-1])
