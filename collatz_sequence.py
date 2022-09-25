# Automate the boring Stuff chapter 3 practice Project - Collatz Seq. - answer.
# Author: Josh Smith

from get_integer import get_integer


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


# Test block
number = get_integer("Please input a number:")
while number != 1:
    number = collatz(number)
    print(number)

# Function Tested and works
