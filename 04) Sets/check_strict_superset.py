"""
TITLE: Check Strict Superset

INPUT:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

OUTPUT:
False

"""

A = set(map(int, input().split()))
for _ in range(int(input())):
    B = set(map(int, input().split()))
    if(A.issuperset(B)):
        continue
    else:
        print('False')
        break
else:
    print('True')
