# Automate the boring Stuff chapter 7 practice Project -
# Regex Version of strip().
# Author: Josh Smith
import re

def regex_strip(a: str, b: str=' ') -> str:
    """Take an input string and a strip character string and remove all
    those strip characters from the beginning and end of the input string

    :param: Input string to process
    :param: Character to strip. Nothing passed will strip white space
    """
    while True:
        strip_lregex = re.compile(r'''^''' + re.escape(b))
        mo1 = re.search(strip_lregex, a)
        if mo1:
            a = re.sub(strip_lregex, '', a)
            continue
        else:
            break
    while True:
        strip_rregex = re.compile(re.escape(b) + r'''$''')
        mo2 = re.search(strip_rregex, a)
        if mo2:
            a = re.sub(strip_rregex, '', a)
            continue
        else:
            break
    
    return a


# test code
test1 = '   3 even spaces   '
test2 = '        uneven spaces   '
test3 = '...dots...'
test4 = '**&stuff*&&*'

test1 = regex_strip(test1)
test2 = regex_strip(test2)
test3 = regex_strip(test3, '.')
test4 = regex_strip(test4, '*&')

print(test1)
print(test2)
print(test3)
print(test4)

# TODO: I think this satisfies the requirement for chapter 7,
#  though need to see if I can fix it to pass strings with multiple
#  characters as the second arg. Something the real .strip() can definitely do.