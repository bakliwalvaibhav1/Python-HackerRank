"""
TITLE: Find the Runner-Up Score!

INPUT:
5
2 3 6 6 5

OUTPUT:
5

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))
