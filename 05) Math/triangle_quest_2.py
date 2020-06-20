"""
TITLE: Triangle Quest 2

INPUT:
5

OUTPUT:
1
121
12321
1234321
123454321

"""

for i in range(1, int(input())+1):
    print((10**i//9)**2)
