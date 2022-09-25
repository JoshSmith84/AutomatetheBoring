#! python3
# big_file_search - Search a directory tree for any files at or over a
# certain size to see if it is unneeded.
# Answer to Chapter 9 Practice Project of Automate the Boring Stuff
# Auther: Josh Smith

import os
from get_integer import get_integer

# get working root folder to scan from (will do test folder for now)
folder = os.getcwd()
convert_num = 0

# get user input on whether they want to search based on MB, GB, TB.
while True:
    byte_size = str(input('Please select byte size type to search for...\n'
                          '1: MB\n'
                          '2: GB\n'
                          '3: TB\n'
                          ': ')
                    )
    if byte_size == '1' or '2' or '3':
        if byte_size == '1':
            byte_size = 'MB'
            convert_num = 1048576
        elif byte_size == '2':
            byte_size = 'GB'
            convert_num = 1073741824
        elif byte_size == '3':
            byte_size = 'TB'
            convert_num = 1099511627776
        else:
            continue
        break
    else:
        continue


# Get size to search for and convert based on input
number = get_integer(f"Please enter the size to search for in {byte_size}'s: ")
print('\n' + ('-' * 35) + 'STATUS' + ('-' * 39))
print(f"Searching {folder} and all sub-folders for any files "
      f"larger than {number}" + f"{byte_size}")

# Convert integer input into bytes
byte_number = number * convert_num

# Walk folder and print out results.
found_count = 0
found_list = []
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filename_path = foldername + '\\' + filename
        try:
            filename_size = os.path.getsize(filename_path)
        except OSError:
            print(f"{filename} does not exist or is inaccessible. Skipping")
            continue
        filename_out_size = str(int(filename_size / convert_num)) \
                            + byte_size + 's'
        if filename_size >= byte_number:
            found_list.append(f"{filename} is {filename_out_size} and "
                  f"resides in {foldername}")
            found_count += 1
print('\n' + ('-' * 35) + 'SUMMARY' + ('-' * 38))
if found_count == 0:
    print('None found')
else:
    print(f'{found_count} occurrence(s) found.')
    print('\n' + ('-' * 35) + 'RESULTS' + ('-' * 38))
    for file in found_list:
        print(file)
print('-' * 80)
print('\nDone')

# Code tested and satisfies project + some. For searching a single folder,
# there is not much utility here as Windows explorer can sort by size already.
# Where this can shine though is the fact that
# it will walk the entire tree from the root of start.
# TODO: add GUI functionality to pick folder and I'd like text box
#  for input number with radial option for MB, GB, etc