#! python3
# 2048.py
'''
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.
'''
# Usage: python 2048.py

from selenium import webdriver

siteUrl = 'https://gabrielecirulli.github.io/2048/'

print('Opening Firefox...')
browser = webdriver.Firefox()

print('Opening ' + siteUrl + '...')
browser.get(siteUrl)


print('Closing Firefox...')
browser.quit()

print('Done')
