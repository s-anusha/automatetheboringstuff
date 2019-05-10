#! python3
# regexVersionOfStrip.py
'''
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''
import re

def regexStrip(toStrip):
	string = toStrip[1]
	if len(toStrip) == 2:
		beginningWhitespaceRegex = re.compile(r'^\s+')
		string = beginningWhitespaceRegex.sub('', string)
		endWhitespaceRegex = re.compile(r'\s+$')
		string = endWhitespaceRegex.sub('', string)
	else:
		substringToRemove = toStrip[2]
		beginningCharactersRegex = re.compile(r'^['+ substringToRemove +']*|['+ substringToRemove +']*$')
		string = beginningCharactersRegex.sub('', string)
	return string

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python regexVersionOfStrip.py string [substring_to_strip]')
    sys.exit()

string = regexStrip(sys.argv)

print('String after stripping: ' + string)


