"""
TITLE: collections.Counter()

INPUT:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

OUTPUT:
200

"""

from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
N = int(input())
shoes = Counter(shoes)

income = 0
for i in range(N):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
