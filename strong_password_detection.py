# Automate the boring Stuff chapter 7 practice Project -
# Strong Password Detection.
# Author: Josh Smith

import re


# Answer Function:
def detect_pass(a: str) -> None:
    """Take a string as input and determine if the string would
    be considered a strong password. For this exercise, a strong
    password is at least eight characters long,
    contains both uppercase and lowercase characters,
    and has at least one digit. Print out True or False as an answer

    :param: string to process and test
    """
    pass_reg = re.compile(r'''(
            [a-z]+
            [A-Z]+
            [0-9]+
            )''', re.VERBOSE)
    if len(a) > 7:
        mo = pass_reg.search(a)
        if mo:
            print(f'{a} is a Good Password')
        else:
            print(f'{a} lacks complexity')
    else:
        print(f'{a} is too short')


# Test code
pass1 = '12345678910'
pass2 = 'pass'
pass3 = 'spamspamspamspamspam'
pass4 = 'PassW0rd1'
pass5 = 'PassW0rd!!'

detect_pass(pass1)
detect_pass(pass2)
detect_pass(pass3)
detect_pass(pass4)
detect_pass(pass5)

# Tested and function works.
# I'd like to add a check for special characters but was not having any luck
# TODO: If I figure out how to do a range of special characters properly,
#  add support for it.