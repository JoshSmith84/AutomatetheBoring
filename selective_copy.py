#! python3
# selective_copy.py - Copies all files in folder tree to a new folder
# based on prompted extension type
# Automate the Boring Stuff Chapter 9 Practice Project
# Author: Josh Smith

import os
import shutil

folder = os.getcwd()
file_type = input(str('Please enter an extension type to organize.\n'
                  'Examples: jpg, pdf, docx, txt\n'
                  ': '))

if file_type[0] != '.':
    file_type = '.' + file_type
file_type_upper = file_type.strip('.').upper()

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        cons_folder = os.path.join(foldername, file_type_upper + 's')
        if file_type in filename:
            print(f"Consolidating {file_type}'s in {foldername}...")
            if os.path.exists(cons_folder) is False:
                os.mkdir(cons_folder)
            shutil.copy(os.path.join(foldername, filename), cons_folder)

# Code tested and works.
# TODO: Add GUI functionality to select root folder then prompt for filetype
# TODO: Add functionality to ignore folders that have already been
#  consolidated when checking again.
# TODO: add choice to copy or move