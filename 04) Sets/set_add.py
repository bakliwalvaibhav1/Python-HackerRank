"""
TITLE: Set.add()

INPUT:
7
UK
China
USA
France
New Zealand
UK
France

OUTPUT:
5

"""

n = int(input())
myset = set()
for _ in range(n):
    myset.add(input())
print(len(myset))

