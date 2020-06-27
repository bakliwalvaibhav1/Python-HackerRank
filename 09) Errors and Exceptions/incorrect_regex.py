"""
TITLE: Incorrect Regex

INPUT:
2
.*\+
.*+

OUTPUT:
True
False

"""

import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)