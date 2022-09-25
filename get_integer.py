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

