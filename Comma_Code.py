# Automate the boring Stuff chapter 4 practice Project - Comma Code - answer.
# Author: Josh Smith


def comma_code(a: list) -> str:
    """Take a list and return a string with all list values
    separated by commas with and at the end. Present the list in normal
    English sentence basically

    :param: Any list of str or int values
    :return: list as string with English grammar
    """
    b = ''
    e = a[-1]
    a.pop(-1)
    for item in a:
        b += str(item) + ', '
    b += f'and {e}.'
    return b


# code to test
spam = [' apples', 'bananas', 'tofu', 'cats', 42]

spam_list = comma_code(spam)
print(spam_list)
# Function tested and works.
