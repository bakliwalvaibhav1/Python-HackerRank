"""
TITLE: ginortS

INPUT:
Sorting1234

OUTPUT:
ginortS1324

"""

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')


