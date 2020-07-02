"""
TITLE: Zipped!

INPUT:
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

OUTPUT:
90.0
91.0
82.0
90.0
85.5

"""

n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) )

for i in zip(*sheet):
    print( sum(i)/len(i) )
