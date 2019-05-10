#! python3
# tablePrinter.py
'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
'''
# Usage: python tablePrinter.py


def printTable(data):
	colWidths = [0] * len(data)
	for i in range(len(data)):
		colWidths[i] = len(max(data[i], key=len))
	amount = int(max(colWidths))
	for i in range(len(data[0])):
		for j in range(len(data)):
			print(data[j][i].rjust(amount), end="")
		print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
