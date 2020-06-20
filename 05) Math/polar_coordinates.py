"""
TITLE: Polar Coordinates

INPUT:
1+2j

OUTPUT:
2.23606797749979
1.1071487177940904

"""

import cmath
z = complex(input())
print(abs(z))
print(cmath.phase(z))
