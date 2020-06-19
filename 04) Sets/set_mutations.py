"""
TITLE: Set Mutations

INPUT:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

OUTPUT:
38

"""

a = int(input())
aSet = set(map(int, input().split()))
n = int(input())
for i in range(n):
    s = input().split()
    command = s[0]
    bSet = set(map(int, input().split()))
    command += "(" + str(bSet) + ")"
    eval('aSet.' + command)
print(sum(aSet))

