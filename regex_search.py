# Automate the boring Stuff Chapter 8 practice project -
# Regex Search
# Write a program that opens all .txt files in a folder and
# searches for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

# Author: Josh Smith

import os
import re

lines = []
folder = os.getcwd()
for file in os.listdir(folder):
    if '.txt' in file:
        with open(file) as in_file:
            temp_data = in_file.read()
            temp_line = ''
            for char in temp_data:
                if char == '\n':
                    lines.append(temp_line)
                    temp_line = ''
                else:
                    temp_line = temp_line + char

reg = input('Please enter a text to search: ')
reg_search = re.compile(reg)
for line in lines:
    mo = reg_search.search(line)
    if mo:
        print(line)

# code tested and works.