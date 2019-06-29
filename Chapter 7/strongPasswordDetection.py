#! python3
# strongPasswordDetection.py
'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''
# Usage: Usage: python strongPasswordDetection.py password

import re

passwordLengthRegex = re.compile(r'^\S{8,}$')	# password is eight characters long
passwordUppercaseRegex = re.compile(r'[A-Z]')	# password contains at least one uppercase character
passwordLowercaseRegex = re.compile(r'[a-z]')	# password contains at least one lowercase character
passwordDigitRegex = re.compile(r'\d')		# password has at least one digit

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python strongPasswordDetection.py password')
    sys.exit()

password = sys.argv[1]

lengthMatch = passwordLengthRegex.search(password)

if lengthMatch is None:
    print('Password should be at least eight characters long.')
    sys.exit()

uppercaseMatch = passwordUppercaseRegex.search(password)

if uppercaseMatch is None:
    print('Password should contain at least one uppercase character.')
    sys.exit()

lowercaseMatch = passwordLowercaseRegex.search(password)

if lowercaseMatch is None:
    print('Password should contain at least one lowercase character.')
    sys.exit()

digitMatch = passwordDigitRegex.search(password)

if digitMatch is None:
    print('Password should have at least one digit.')
    sys.exit()

print('Password accepted.')
