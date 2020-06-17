"""
TITLE: Python If-Else

INPUT:
12

OUTPUT:
Weird

"""

if __name__ == '__main__':
    n = int(input().strip())
    if(n%2 != 0):
        print("Weird")
    else:
        if(n>=6 and n<= 20):
            print("Weird")
        else:
            print("Not Weird")
