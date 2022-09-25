#! python3
# fill_gaps.py - Search a single folder for any files
# with numbering after a uniform prefix.
# Then if there are any gaps,
# rename the next lowest file to next number until there are no more gaps.
# Answer to Chapter 9 Practice Project of Automate the Boring Stuff
# Auther: Josh Smith

import os
import re
import sys

# get folder to scan (using special test folder)
# The test folder contains multiple prefixes with different leading 0's
# some prefixes with no duplicates and some prefixes with no gaps.
# Therefore test folder handles all edge cases
folder = 'U:\\Joshua\\Dropbox\\Dropbox\\' \
         'Python\\AutomatetheBoring\\testfiles\\gap_test - bk\\'

#  iterate in folder and check for similar prefixes.
#  Group all found into list
filenames = os.listdir(folder)
prefix_detect = re.compile(r"""^(.*?)(\d+)(\.)+(.*?)$""")
found_prefixes = []
for files in filenames:
    mo = re.search(prefix_detect, files)
    if mo:
        found_prefixes.append(mo.group(1))

# Figure out which prefix(es) in the prefix list has a duplicate,
#  put one of each into a new list
prefixes = []
i = 0
while i < len(found_prefixes):
    j = i + 1
    while j < len(found_prefixes):
        if found_prefixes[i] == found_prefixes[j]:
            if found_prefixes[i] not in prefixes:
                prefixes.append(found_prefixes[i])
            j += 1
        else:
            j += 1
    i += 1

#  Exit program if none found.
if len(prefixes) == 0:
    sys.exit("There were no applicable files found. Program terminated...")

# Create regex based on any found common prefix and
#  look for said prefix in original file list
for prefix in prefixes:
    str_numbers = []
    prefix_regex = re.compile((rf"""^({prefix})(\d+)(\.)+(.*?)$"""))
    for files in filenames:
        mo = re.search(prefix_regex, files)
        if mo:
            str_numbers.append(mo.group(2))

    # Figure out how many (if any) leading zeros there are
    lead0 = 0
    for number in str_numbers:
        lead0_temp = 0
        for char in number:
            if char == '0':
                lead0_temp += 1
        if lead0_temp > lead0:
            lead0 = lead0_temp
    r_just_amount = lead0 + 1

    # Keep a count so we know what number to give to fill gap.
    #  I wanted to see if I could wrap this in the mo check above the
    #  rjust check but I think the best way here is to go ahead and
    #  rename once the gap is found.
    #  And to do that, need rjust info first
    file_count = 0

    # Iterate over file names looking for bigger than current expected.
    #  once found, rename to expected and continue to exhaust list.
    for files in filenames:
        mo = re.search(prefix_regex, files)
        if mo:
            file_count += 1
            if int(mo.group(2)) > file_count:
                print(f"renaming {files} to {mo.group(1)}" +
                      f"{str(file_count).rjust(r_just_amount, '0')}" +
                      f"{mo.group(3)}" + f"{mo.group(4)}")
                os.rename(folder + files, folder + f"{mo.group(1)}" +
                      f"{str(file_count).rjust(r_just_amount, '0')}" +
                      f"{mo.group(3)}" + f"{mo.group(4)}")

# Code tested and works!!!
# I'm not sure if I could have done this more efficiently or with less code yet,
# but it works as intended.
# It will handle multiple prefix types as well and only if they are numbered and
# only if they share prefix.
# Each detected prefix is wrapped in its own for loop
# which is how it can handle multiple types.