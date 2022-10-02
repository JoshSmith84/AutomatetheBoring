#! python3
# lucky.py - Opens several Google search results.
# Credit to Al Sweigart from Automate The Boring Stuff for most of this code.

# However, Google had clearly updated their site
# since the 1st edition was written, and I spent
# a few hours trying to figure out what class to pass for soup.select.
# I learned quite a bit about CSS and HTML in the process and
# feel much more comfortable parsing elements to do my own web scraping with
# Beautiful Soup in the future. So this was sort of a practice project for me.

import requests
import sys
import webbrowser
import bs4
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %'
                                                '(levelname)s - %'
                                                '(message)s',
                    filename='program_logging.txt')
logging.disable(logging.CRITICAL)

print('Googling...') # display text while downloading the Google page.
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug(f'Google link = {res}')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='lxml')

# Open a browser tab for each result.
linkElems = soup.select('.egMi0 a')
logging.debug(f'Found link Elements: {linkElems}')
num_open = min(5, len(linkElems))
logging.debug(f'Links to open: {num_open}')
for i in range(num_open):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    logging.debug('Opening: https://google.com' + linkElems[i].get('href'))