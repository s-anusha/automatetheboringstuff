#! python3
# deletingUnneededFiles.py
'''
Write a program that walks through a folder tree and searches for exceptionally large files or folders - say, ones that have a file size of more than 100MB. (Remember, to get a file's size, you can use os.path.getsize() from the os.module.) Print these files with their absolute path to the screen.
'''
# Usage: python deletingUnneededFiles.py sizeInBytes


import sys, os

if len(sys.argv) < 2:
	print('Usage: python deletingUnneededFiles.py sizeInBytes')
	sys.exit()

size = sys.argv[1]

print('Enter folder path: ')
sourceFolder = raw_input()
print('\n')

for folderName, subfolders, filenames in os.walk(sourceFolder):
	for filename in filenames:
		filepath = os.path.join(folderName,filename)
		print(filepath)
		print(os.path.getsize(filepath)
		#if os.path.getsize(filepath) > size:
		#	print(os.path.abspath(filename))
