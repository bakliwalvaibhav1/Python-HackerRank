"""
TITLE: itertools.combinations()

INPUT:
HACK 2

OUTPUT:
A
C
H
K
AC
AH
AK
CH
CK
HK

"""

import itertools
S, k = (input().split())

for i in range(1, int(k)+1):
    op = list(itertools.combinations(sorted(S), i))
    for i in op:
        print(''.join(i))
