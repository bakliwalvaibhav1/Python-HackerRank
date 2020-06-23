"""
TITLE: itertools.combinations_with_replacement()

INPUT:
HACK 2

OUTPUT:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""

import itertools
S, k = (input().split())

op = list(itertools.combinations_with_replacement(sorted(S), int(k)))
for i in op:
    print(''.join(i))
