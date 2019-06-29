#! python3
# madLibs.py
'''
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''
# Usage: python madLibs.py input_file [output_file]

import sys, re

if len(sys.argv) < 2:
	print('Usage: python madLibs.py input_file [output_file]')

infile = open(sys.argv[1], 'r')

if len(sys.argv) >  2:
	outfile = open(sys.argv[2], 'w')
else:
	outfile = open('output.txt', 'w')

wordRegex = re.compile(r'\w+')

for line in infile:
	for word in line.split():
		source = wordRegex.search(word)
		if source.group() == 'ADJECTIVE':
			print('Enter an adjective:')
			newWord = raw_input()
			line = line.replace(word, newWord)
		elif source.group() == 'NOUN':
			print('Enter a noun:')
			newWord = raw_input()
			line = line.replace(word, newWord)
		elif source.group() == 'ADVERB':
			print('Enter an adverb:')
			newWord = raw_input()
			line = line.replace(word, newWord)
		elif source.group() == 'VERB':
			print('Enter an verb:')
			newWord = raw_input()
			line = line.replace(source.group(), newWord)
	outfile.write(line)

infile.close()
outfile.close()

print('Output:')
outfile = open('output.txt', 'r')
print outfile.read()
outfile.close()
