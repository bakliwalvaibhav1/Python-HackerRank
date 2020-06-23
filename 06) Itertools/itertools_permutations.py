"""
TITLE: itertools.permutations()

INPUT:
HACK 2

OUTPUT:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""

import itertools
S, k = (input().split())
op = list(itertools.permutations(S, int(k)))
op = sorted(op)
for i in op:
    print(''.join(i))
