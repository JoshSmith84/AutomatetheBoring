# Automate the boring Stuff chapter 8 practice Project -
# Mad Libs.
# Author: Josh Smith

import re

# open input file and read
with open('madlib-input.txt', 'r') as in_file:
    mad_text = in_file.read()

# define regex
libs = re.compile(r'''(ADJECTIVE)|(NOUN)|(ADVERB)|(VERB)''')

# iterate through text and prompting for mad lib replacement until all
# options are exhausted
while True:
    mo = libs.search(mad_text)
    if mo:
        if mo.group()[0] == 'A':
            answer = input(f'Please enter an {mo.group().casefold()}:\n')
        else:
            answer = input(f'Please enter a {mo.group().casefold()}:\n')
        mad_text = libs.sub(answer, mad_text, 1)
    else:
        break

with open('madlib-output.txt', 'w') as out_file:
    out_file.write(mad_text)

# code tested and works.