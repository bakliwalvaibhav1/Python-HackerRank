"""
TITLE: Check Subset

INPUT:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

OUTPUT:
True
False
False

"""

T = int(input())
for _ in range(T):
    a = int(input())
    aSet = set(map(int, input().split()))
    b = int(input())
    bSet = set(map(int, input().split()))
    print(aSet.issubset(bSet))

