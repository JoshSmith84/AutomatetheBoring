# multiplicationTable.py takes a number N from the command line
# and creates an N × N multiplication table in an Excel spreadsheet.
# usage: py multiplicationTable.py 6

# Author: Josh Smith

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, NamedStyle
import sys
import os

# get valid integer passed via cmd. reject incorrect with error

# With valid int, create spreadsheet with colA and



class MultTable():

    def __init__(self, number=1):
        wb = Workbook()
        wb_file = f'{number}.xlsx'
        wb.save(wb_file)
        wb = load_workbook(wb_file)
        sheet = wb['Sheet']
        ft = Font(bold=True)
        # row1 listing all integers greater than 1 to the passed integer
        # row1 and colA should be bold
        for i in range(number + 1):
            sheet.cell(row=i + 1, column=1).value = i
            sheet.cell(row=i + 1, column=1).font = ft
            sheet.cell(row=1, column=i + 1).value = i
            sheet.cell(row=1, column=i + 1).font = ft
        # then have products of each row/col in the grid
            for n in range(1, number + 1):
                sheet.cell(row=i + 1, column=n + 1).value = i * n
            sheet.cell(row=1, column=1).value = None
        wb.save(wb_file)


# then have products of each row/col in the grid

# save the sheet then finished.

# In progress test code
test = MultTable(4)