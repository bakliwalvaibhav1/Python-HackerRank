"""
TITLE: Collections.deque()

INPUT:
6
append 1
append 2
append 3
appendleft 4
pop
popleft

OUTPUT:
1 2

"""

from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
