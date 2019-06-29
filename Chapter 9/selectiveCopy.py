#! python3
# selectiveCopy.py
'''
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
'''
# Usage: python selectiveCopy.py .extension

import sys, os, shutil

if len(sys.argv) < 2:
	print('Usage: python selectiveCopy.py .extension')
	sys.exit()

extension = sys.argv[1]

print('Enter source folder path: ')
sourceFolder = raw_input()
print('Enter destination folder path: ')
destinationFolder = raw_input()
print('\n')

for folderName, subfolders, filenames in os.walk(sourceFolder):
	for filename in filenames:
		if filename.endswith(extension):
			filepath = os.path.join(folderName,filename)
			shutil.copy(original, destinationFolder)
			print('Copied ' + filepath + ' to ' + destinationFolder)
