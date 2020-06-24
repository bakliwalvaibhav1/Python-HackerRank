"""
TITLE: Collections.namedtuple()

INPUT:
5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5

OUTPUT:
78.00

"""

from collections import namedtuple

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
