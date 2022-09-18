# Automate the boring Stuff chapter 3 practice Project - Collatz Seq. - answer.
# Author: Josh Smith

# Answer to project
def collatz(col_num: int) -> int:
    """Determines if input is even or odd, then runs appropriate
    collatz formula and returns the result

    ":param: integer to check and process
    :return: new integer after processing"""

    if col_num % 2 == 0:
        col_num = col_num // 2
    else:
        col_num = 3 * col_num + 1

    return col_num


# Pulled from another practice program I wrote to help test
def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).
    The function will continue looping, and prompting
    the user,until a valid `int` is entered.

    :param prompt: The String that the user will see
         when they're prompted to enter the value.
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a valid number".format(temp))


# Test block
number = get_integer("Please input a number:")
while number != 1:
    number = collatz(number)
    print(number)

# Function Tested and works
