"""
TITLE: Map and Lambda Function

INPUT:
5

OUTPUT:
[0, 1, 1, 8, 27]

"""

cube = lambda x: x*x*x # complete the lambda function

def fibonacci(n):
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))