#! python3
# linkVerification.py
'''
Write a program that, given the URL of a web page, will attempt to download every linked page on the page. The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
'''
# Usage: python linkVerification.py site_url

from selenium import webdriver
import sys

if len(sys.argv) < 2:
  print('Usage: python linkVerification.py site_url")
	sys.exit()

siteUrl = sys.argv[1]

print('Opening Firefox...')
browser = webdriver.Firefox()

print('Opening ' + siteUrl + '...')
browser.get(siteUrl)

print('Downloading linked pages...')
linkElements = browser.find_elements_by_tag_name('a')
for i in range (linkElements)
  

print('Closing Firefox...')
browser.quit()

print('Done')
