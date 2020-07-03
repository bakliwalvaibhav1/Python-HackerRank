"""
TITLE: Reduce Function

INPUT:
3
1 2
3 4
10 6

OUTPUT:
5 8

"""

from fractions import Fraction
from functools import reduce
import operator

def product(fracs):
    t =  reduce(operator.mul , fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

