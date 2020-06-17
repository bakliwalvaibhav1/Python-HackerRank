"""
TITLE: Lists

INPUT:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

OUTPUT:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        command = s[0]
        args = s[1:]
        if command !="print":
            command += "("+ ",".join(args) +")"
            eval("l."+command)
        else:
            print (l)
