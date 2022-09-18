# Automate the boring Stuff chapter 6 practice Project -
# Table Printer.
# Author: Josh Smith


# Answer function:
def print_table(a: list) -> None:
    """Pass a list of lists as input. Print out the list in a neat table
    with all items right justified. Each internal list will make up
    each column of the final display.

    :param: A list of lists of strings
    """
    # initialize local variables
    col_widths = []

    # Find the longest string in each inner list and creat a list of integers
    for li in a:
        temp_width = 0
        for item in li:
            if len(item) > temp_width:
                temp_width = len(item)
        col_widths.append(temp_width)
    print(col_widths)

    # process strings
    for l in range(len(a[0])):
        for n in range(len(a)):
            print(f'{a[n][l].rjust(col_widths[n])}', end=' | ')
        print()


# List of lists to test with:

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
    ['jet', 'airbus', 'shuttle', 'duster', 'drone'],
]

print_table(tableData)

# Function tested good. I even had to go through it after I tested again
# to understand what I did, but the solution is correct.
# Also, countless new lists of strings may be added to the parent list,
# and this will still work. It will only work with lists of 4 items
# though, and would need to be fixed to allow different sized lists.
# TODO: get length of longest inner list and
# TODO: pass for outer loop range and handle lists not as long.
