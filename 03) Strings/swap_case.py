"""
TITLE: sWAP cASE

INPUT:
HackerRank.com presents "Pythonist 2".

OUTPUT:
hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)