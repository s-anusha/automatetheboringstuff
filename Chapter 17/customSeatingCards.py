#! python3
# customSeatingCards.py
'''
Chapter 13 included a practice project to create custom invitations from a list of guests in a plaintext file. As an additional project, use the pillow module to create images for custom seating cards for your guests. For each of the guests listed in the guests.txt file from the resources at http://nostarch.com/automatestuff/, generate an image file with the guest name and some flowery decoration. A public domain flower image is available in the resources at http://nostarch.com/automatestuff/.

To ensure that each seating card is the same size, add a black rectangle on the edges of the invitation image so that when the image is printed out, there will be a guideline for cutting. The PNG files that Pillow produces are set to 72 pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.
'''
# Usage: python customSeatingCards.py

import os
from PIL import Image, ImageDraw

file = open('guests.txt', 'r')
guestList = []
for line in file:
    guestList.append(line.strip())

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'flower.jpg'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('invitations', exist_ok=True)

for guest in guestList:
    im = Image.new('RGBA', (288, 360), 'white')
    width, height = im.size
    draw = ImageDraw.Draw(im)
    textWidth, textHeight = draw.textsize(guest)
    if (width - logoWidth < textWidth or height - logoHeight < textHeight):
        continue
    im.paste(logoIm, (width - logoWidth - 1, height - logoHeight - 1))
    draw.text((1, 1), guest, fill='black')
    draw.rectangle((0, 0, 287, 359), outline='black')
    im.save(os.path.join('invitations', guest) + '.png')

