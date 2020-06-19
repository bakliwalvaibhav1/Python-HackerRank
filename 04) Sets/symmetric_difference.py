"""
TITLE: Symmetric Difference

INPUT:
4
2 4 5 9
4
2 4 11 12

OUTPUT:
5
9
11
12

"""

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
c = set(list(a.difference(b)) + list(b.difference(a)))
print('\n'.join([str(i) for i in sorted(c)]))
