"""
TITLE: What's Your Name?

INPUT:
Ross
Taylor

OUTPUT:
Hello Ross Taylor! You just delved into python.

"""

def print_full_name(a, b):
    print("Hello {fname} {lname}! You just delved into python.".format(fname=a, lname=b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)