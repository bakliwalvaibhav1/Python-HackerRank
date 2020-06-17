"""
TITLE: Write a Function

INPUT:
1990

OUTPUT:
False

"""

def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 != 0):
            leap = True
        if (year % 400 == 0):
            leap = True

    # Write your logic here

    return leap

