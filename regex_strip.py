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
    strip_lregex = re.compile(r"^[" + re.escape(b) + "]")
    strip_rregex = re.compile(r"[" + re.escape(b) + r"]$")
    while True:
        mo1 = re.search(strip_lregex, a)
        if mo1:
            a = re.sub(strip_lregex, '', a)
            continue
        else:
            break
    while True:
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
test5 = 'spmaHello worldspam'

print(regex_strip(test1))
print(regex_strip(test2))
print(regex_strip(test3, '.'))
print(regex_strip(test4, '*&'))
print(regex_strip(test5, 'spma'))

# TODO: It works as intended though I'm sure there is a way to shape
#  the regex in one line and sub it all together as well.