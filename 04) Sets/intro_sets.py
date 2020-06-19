"""
TITLE: Introduction to Sets

INPUT:
10
161 182 161 154 176 170 167 171 170 174

OUTPUT:
169.375

"""

def average(array):
    myset = set(array)
    return(sum(myset)/len(myset))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)