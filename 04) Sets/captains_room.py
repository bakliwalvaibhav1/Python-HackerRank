"""
TITLE: The Captain's Room

INPUT:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

OUTPUT:
8

"""

K = int(input())
rooms = list(map(int, input().split()))

single, multiple = set(), set()
for room in rooms:
    single.add(room) if room not in single else multiple.add(room)
print(single.difference(multiple).pop())

