"""
TITLE: Text Wrap

INPUT:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

OUTPUT:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

import textwrap

def wrap(string, max_width):
    return("\n".join((textwrap.wrap(string ,width=max_width))))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
