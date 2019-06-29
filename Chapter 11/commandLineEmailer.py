#! python3
# commandLineEmailer.py - untested
'''
Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.
'''
# Usage: python commandLineEmailer.py email_address message_string

from selenium import webdriver
import sys

if len(sys.argv) < 3:
  print('Usage: python commandLineEmailer.py email_address message_string")
	sys.exit()

emailId = sys.argv[1]
messageString = sys.argv[2]

print('Opening Firefox...')
browser = webdriver.Firefox()

print('Opening Gmail...')
browser.get('https://gmail.com')

print('Signing in...')
signInElement = browser.find_element_by_link_text('Sign in')
signInElement.click()

usernameElement = browser.find_element_by_name('identifier')
usernameElement.send_keys(myEmailId@gmail.com)
usernameElement.send_keys(Keys.ENTER)

passwordElement = browser.find_element_by_name('password')
passwordElement.send_keys(myPassword)
passwordElement.send_keys(Keys.ENTER)

print('Composing email...')
emailElement = browser.find_element_by_class('T-I J-J5-Ji T-I-KE L3')
emailElement.click()

#toElement = browser.find_element_by_name('to')
emailElement.send_keys(emailId)
emailElement.send_keys(Keys.TAB)

#subjectElement = broswer.find_element_by_name('subjectelement')
emailElement.send_keys('Sent from the command line')
emailElement.send_keys(Keys.TAB)

#messageElement = browser.find_element_by_id(':am')
emailElement.send_keys(messageString)
emailElement.send_keys(Keys.TAB)

print('Sending email...')
emailElement.send_keys(Keys.ENTER)

print('Signing out...')
emailElement = browser.find_element_by_class('gb_x gb_Ea gb_f')
emailElement.click()
emailElement = browser.find_element_by_link_text('Sign out')
emailElement.click()

print('Closing Firefox...')
browser.quit()

print('Done')
