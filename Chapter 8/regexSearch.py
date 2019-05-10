#! python3
# regexSearch.py
'''
Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.
'''
# Usage: python regexSearch.py


import os, re

print('Enter regular expression: ')
userRegex = input()
searchRegex = re.compile(userRegex)
print('\n')

for file in os.listdir("."):
    if file.endswith(".txt"):
	print(file)
        checkFile = open(file, 'r')
	for line in checkFile:
		found = searchRegex.findall(line)
		print(found)
	checkFile.close()
	print('\n')
