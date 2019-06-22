#! python3
# excel-To-CSV-Converter.py
'''
Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you had to convert hundreds of Excel files to CSVs, it would take hours of clicking. Using the openpyxl module from Chapter 12, write a program that reads all the Excel files in the current working directory and outputs them as CSV files.

A single Excel file might contain multiple sheets; you’ll have to create one CSV file per sheet. The filenames of the CSV files should be <excel filename>_<sheet title>.csv, where <excel filename> is the filename of the Excel file without the file extension (for example, 'spam_data', not 'spam_data.xlsx') and <sheet title> is the string from the Worksheet object’s title variable.

This program will involve many nested for loops. The skeleton of the program will look something like this:

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                # Append each cell's data to rowData.

            # Write the rowData list to the CSV file.

        csvFile.close()
Download the ZIP file excelSpreadsheets.zip from http://nostarch.com/automatestuff/, and unzip the spreadsheets into the same directory as your program. You can use these as the files to test the program on.
'''
# Usage: python excel-To-CSV-Converter.py

import openpyxl
import os
import csv

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        csvFilename = excelFile[:len(excelFile)-5] + '_' + sheet.title + '.csv'
        csvFile = open(csvFilename, 'w', newline='')
        # Create the csv.writer object for this CSV file.
        csvWriter = csv.writer(csvFile)
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet[rowNum, colNum])
            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
        csvFile.close()
    wb.close()

