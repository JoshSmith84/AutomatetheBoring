# Automate the boring Stuff chapter 4 practice Project -
# Character Picture Grid - answer.
# Author: Josh Smith

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ]


for char in range(len(grid[0])):
    for li in grid:
        print(li[char], end='')
    print()


# This is so much cleaner than my old solution
# in which I made a function for the internal loop...
# Confirmed it works.
