#! python3
# imageSiteDownloader.py - untested
'''
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
'''
# Usage: python imageSiteDownloader.py site_url search_category

from selenium import webdriver
import sys

if len(sys.argv) < 3:
  print('Usage: python imageSiteDownloader.py site_url search_category")
	sys.exit()

#siteUrl = sys.argv[1]
siteUrl = 'https://www.flickr.com/'
searchCategory = sys.argv[2]

print('Opening Firefox...')
browser = webdriver.Firefox()

print('Opening ' + siteUrl + '...')
browser.get(siteUrl)

print('Searching for ' + searchCategory + '...')
searchElement = browser.find_element_by_link_id('search-field')
searchElement.send_keys(searchCategory)
searchElement.send_keys(Keys.ENTER)

# print('Filtering by creative commons license...')
# licenseElement = browser.find_element_by_class('filter-license')
# licenseELement.click()
# click All creative commons

print('Downloading images...')
imageElements = browser.find_elements_by_partial_link_text('/photos/')
for i in range(imageElements):
  imageElements[i].click()
  downloadElement = browser.find_element_by_class('download')
  downloadElement.click()
  sizeElement = browser.find_element_by_link_text('View all sizes')
  sizeElement.click()
  try:
    originalElement = browser.find_element_by_link_text('Original')
    originalElement.click()
    downloadLinkElement = browser.find_element_by_link_text('Download the Original size of this photo')
    downloadlinkElement.click()
  except NoSuchElement:
    continue
        
print('Closing Firefox...')
browser.quit()

print('Done')
