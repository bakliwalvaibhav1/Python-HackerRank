"""
TITLE: Nested Lists

INPUT:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

OUTPUT:
Berry
Harry

"""

if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))

