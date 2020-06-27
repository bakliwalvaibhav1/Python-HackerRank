"""
TITLE: Calendar Module

INPUT:
08 05 2015

OUTPUT:
WEDNESDAY

"""

import calendar

m, d, y = map(int, input().split())
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
