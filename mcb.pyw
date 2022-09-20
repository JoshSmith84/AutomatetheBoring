#! python
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw delete <keyword> - Deletes keyword.
# py.exe mcb.pyw list - loads all keywords to clipboard.
# py.exe mcb.pyw deleteall - deletes all keywords.
# credit to :Al Sweigart. Automate the Boring Stuff with Python
# Practical Programming for Total Beginners No Starch Press. for base code

# Chapter 8 practice project to add delete statements.

import pyperclip
import shelve
import sys

# Save clipboard content
with shelve.open('mcb') as mcb_shelf:
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Chapter 8 project addition 1
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        # Chapter 8 project addition 2
        elif sys.argv[1].lower() == 'deleteall':
            mcb_shelf.clear()
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])

# Delete statements added and tested. Code works.