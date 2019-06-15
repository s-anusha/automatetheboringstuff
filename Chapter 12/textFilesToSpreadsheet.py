#! python3
# textFilesToSpreadsheet.py
'''
Write a program to read in the contents of several text files (you can make the text files yourself) and insert those contents into a spreadsheet, with one line of text per row. The lines of the first text file will be in the cells of column A, the lines of the second text file will be in the cells of column B, and so on.
Use the readlines() File object method to return a list of strings, one string per line in the file. For the first file, output the first line to column 1, row 1. The second line should be written to column 1, row 2, and so on. The next file that is read with readlines() will be written to column 2, the next file to column 3, and so on.
'''
# Usage: python textFilesToSpreadsheet.py

import openpyxl
import os

wbWrite = openpyxl.Workbook()
writeSheet = wbWrite.active
rowNumber = 1
columnNumber = 1

for fileName in os.listdir(os.getcwd()):
    if fileName.endswith('.txt'):
        file = open(fileName, 'r')
        lines = file.readlines()
        for line in lines:
            writeSheet.cell(row=rowNumber, column=columnNumber).value = line
            rowNumber += 1
        columnNumber += 1
        rowNumber = 1
        file.close()

wbWrite.save('textFilesToSpreadsheet.xlsx')
