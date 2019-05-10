#! python3
# extendingTheMulticlipboard.py
'''
Extend the multiclipboard program in this chapter so that it has a delete <keyword> command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.
'''
# Usage: python extendingTheMulticlipboard.py save keyword - Saves clipboard to keyword.
#        python extendingTheMulticlipboard.py keyword - Loads keyword to clipboard.
#        python extendingTheMulticlipboard.py list - Loads keyword list to clipboard.
#        python extendingTheMulticlipboard.py delete keyword - Deletes keyword from shelf.
#        python extendingTheMulticlipboard.py delete - Deletes all keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
		print('Saved to shelf from clipboard as ' + sys.argv[2])
	elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
		print(sys.argv[2] + ' deleted from shelf.')
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
        	pyperclip.copy(str(list(mcbShelf.keys())))
		print('Shelf keyword list copied to clipboard.')
	elif sys.argv[1].lower() == 'delete':
		for key in mcbShelf:
			del mcbShelf[key]
        	print('All keywords deleted from shelf.')
       	elif sys.argv[1] in mcbShelf:
        	pyperclip.copy(mcbShelf[sys.argv[1]])
		print(sys.argv[1] + ' value copied from shelf to clipboard.')
	else:
		print('Invalid.')
else:
	print('''\nUsage:
		python extendingTheMulticlipboard.py save keyword - Saves clipboard to keyword.
		python extendingTheMulticlipboard.py keyword - Loads keyword to clipboard.
		python extendingTheMulticlipboard.py list - Loads keyword list to clipboard.
		python extendingTheMulticlipboard.py delete keyword - Deletes keyword from shelf.
		python extendingTheMulticlipboard.py delete - Deletes all keywords.''')

mcbShelf.close()
