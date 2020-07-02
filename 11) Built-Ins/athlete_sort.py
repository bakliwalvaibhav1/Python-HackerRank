"""
TITLE: Athlete Sort

INPUT:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

OUTPUT:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""

N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)


