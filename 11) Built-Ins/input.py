"""
TITLE: Input()

INPUT:
1 4
x**3 + x**2 + x + 1

OUTPUT:
True

"""

ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))