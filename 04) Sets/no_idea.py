"""
TITLE: No Idea!

INPUT:
3 2
1 5 3
3 1
5 7

OUTPUT:
1

"""

n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))

