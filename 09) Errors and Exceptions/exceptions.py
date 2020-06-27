"""
TITLE: Exceptions

INPUT:
3
1 0
2 $
3 1

OUTPUT:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

"""

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
