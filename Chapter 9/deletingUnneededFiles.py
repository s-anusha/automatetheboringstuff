#! python3
# deletingUnneededFiles.py
'''
It's not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you're trying to free up room on your computer, you'll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders-say, ones that have a file size of more than 100MB. (Remember, to get a file's size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
'''
# Usage: python deletingUnneededFiles.py sizeInBytes

import sys, os

if len(sys.argv) < 2:
	print('Usage: python deletingUnneededFiles.py sizeInBytes')
	sys.exit()

size = sys.argv[1]
size = int (size)

print('Enter folder path: ')
sourceFolder = raw_input()
print('\n')

print('Files to delete:')
for folderName, subfolders, filenames in os.walk(sourceFolder):
	for filename in filenames:
		filepath = os.path.join(folderName, filename)
		fileSize = os.path.getsize(filepath)
		if fileSize > size:
			print(filepath)

