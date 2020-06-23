"""
TITLE: Compress the String!

INPUT:
1222311

OUTPUT:
(1, 1) (3, 2) (1, 3) (2, 1)

"""

import itertools
S = input()
print(*[(len(list(c)), int(k)) for k, c in itertools.groupby(S)])