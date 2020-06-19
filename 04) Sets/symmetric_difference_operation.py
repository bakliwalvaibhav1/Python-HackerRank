"""
TITLE: Set.symmetric_difference() Operation

INPUT:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

OUTPUT:
8

"""

e = int(input())
eSet = set(map(int, input().split()))
f = int(input())
fSet = set(map(int, input().split()))
print(len(eSet.symmetric_difference(fSet)))

