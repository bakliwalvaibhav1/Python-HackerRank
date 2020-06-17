"""
TITLE: List Comprehensions

INPUT:
1
1
1
2

OUTPUT:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n])


