"""
TITLE: The Minion Game

INPUT:
BANANA

OUTPUT:
Stuart 12

"""


def minion_game(string):
    vowels = 'aeiouAEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)
    if kevin>stuart:
        print("Kevin", kevin)
    elif stuart>kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)