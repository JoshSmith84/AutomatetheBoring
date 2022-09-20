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
    and has at least one digit. Print out result of test.

    :param: string to process and test
    """
    pass_reg = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[!-~]{8,}$')

    mo = pass_reg.findall(a)
    if mo:
        print(f'{a}: is a Good Password')
    else:
        print(f'{a}: lacks length or complexity')


# Test code
passes = ['12345678910',
          'pass',
          'spamspamspamspamspam',
          'PassWord1',
          '13passWord']

for pas in passes:
    detect_pass(pas)

# Tested and function works.
# I'd like to add a check for special characters but was not having any luck
# TODO: If I figure out how to do a range of special characters properly,
#  add support for it.
