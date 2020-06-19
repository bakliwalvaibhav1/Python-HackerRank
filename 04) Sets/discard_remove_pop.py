"""
TITLE: Set.discard(), .remove() & .pop()

INPUT:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

OUTPUT:
4

"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    l = input().split()
    command = l[0]
    args = l[1:]
    command += "("+ ",".join(args) +")"
    eval("s."+command)

print(sum(s))