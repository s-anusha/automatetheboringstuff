#! python3
# scheduledWebComicDownloader.py
'''
Write a program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit. Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X, and cron on Linux) can run your Python program once a day. The Python program itself can download the comic and then copy it to your desktop so that it is easy to find. This will free you from having to check the website yourself to see whether it has updated. (A list of web comics is available at http://nostarch.com/automatestuff/.)
'''
# Usage: python scheduledWebComicDownloader.py

import requests, os, bs4

urlDict = {'http://www.lefthandedtoons.com/':   'Left-handed Toons',
           'http://www.savagechickens.com/': 'Savage Chickens',
           'http://www.lunarbaboon.com': 'Lunar Baboon',
           'http://completelyseriouscomics.com/': 'Completely Serious Comics',
           'http://www.exocomics.com/': 'Extra Ordinary',
           'http://nonadventures.com/': 'Wonderella',
            'http://www.happletea.com/': 'Happle Tea'}

linkSelector = {'http://www.lefthandedtoons.com/': '.comicimage',
                'http://www.savagechickens.com/': '.entry_content p img',
                'http://www.lunarbaboon.com': '.full-image-block img',
                'http://completelyseriouscomics.com/': '#comic-1 img',
                'http://www.exocomics.com/': '.comic img',
                'http://nonadventures.com/': '#comic img',
                'http://www.happletea.com/': '#comic img'}


def getSelector(link):
    return linkSelector.get(link, None)


def getComicUrl(link, comicElem):
    if link == 'http://www.lunarbaboon.com':
        comicUrl = link + comicElem[0].get('src')
        baseName = os.path.basename(comicUrl).split('?__')[0]
        return comicUrl, baseName
    else:
        comicUrl = comicElem[0].get('src')
        baseName = os.path.basename(comicUrl)
        return comicUrl, baseName


for site in urlDict.values():
    os.makedirs(site, exist_ok=True)   # store comics in ./url

for link in urlDict.keys():
    if not link.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % link)
        res = requests.get(link)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        # Find the URL of the comic image.
        # comicElem = soup.select('#comic img')
        comicElem = soup.select(getSelector(link))
        if comicElem == []:
            print('Could not find comic image.')
        else:
            try:
                comicUrl, baseName = getComicUrl(link, comicElem)
                if comicUrl is None or baseName is None:
                    continue
                if os.path.isfile(os.path.join(urlDict[link], baseName)):
                    # If image already, exists, do nothing
                    print('Image %s already exists.' % (comicUrl))
                    continue
                else:
                    # Download the image.
                    print('Downloading image %s...' % (comicUrl))
                    res = requests.get(comicUrl)
                    res.raise_for_status()
                    # Save the image to ./link.
                    imageFile = open(os.path.join(urlDict[link], baseName), 'wb')
                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
            except requests.exceptions.MissingSchema:
                # skip this comic
                continue
print('Done.')

