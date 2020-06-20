"""
TITLE: Find Angle MBC

INPUT:
10
10

OUTPUT:
45°

"""

import math
AB = int(input())
BC = int(input())
degree_sign= u'\N{DEGREE SIGN}'
print(str(round(math.degrees(math.atan(AB/BC))))+degree_sign)
