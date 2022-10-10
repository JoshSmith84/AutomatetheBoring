# Automate the Boring Stuff Chapter 11 Practice Project 2
# imgur_search.py - utilize Beautiful Soup to  search imgur,
# and download all images in the first page to a folder.
# TODO Add support for downloading entire gallery
# TODO Add support for gifs(right now downloads some but extension would
#  need to be changed in order for animation to work.
# TODO Possible at all to do this hidden with script heavy sites?

# example: py.exe imgur_search.py Search term

# Author: Josh Smith

# imports
import logging
import sys
import bs4
import os
import requests
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %'
                                                '(levelname)s - %'
                                                '(message)s',
                    filename='program_logging.txt')

logging.disable(logging.CRITICAL)

# Initialize any variables
search = ''
folder = 'U:\\Joshua\\Dropbox\\Dropbox\\Pictures\\Automated Downloads'
browser = webdriver.Chrome(ChromeDriverManager().install())
image_elem = ''
file_count = 0
date_list = str(datetime.datetime.today()).split(' ')
date = date_list[0]

# Get sys args and handle multiple words
# Handle different inputs and searches with more than one word
if len(sys.argv) < 2:
    sys.exit('Missing required search argument. Closing Program')
elif len(sys.argv) > 2:
    for word in sys.argv[1:]:
        for char in word:
            search += char
        search += '+'
    search = search.strip('+')
else:
    search = sys.argv[1]

# Check if folder exists in pictures folder. If not, create the folder
if os.path.exists(folder + '\\' + search) is False:
    os.makedirs(folder + '\\' + search)
folder = folder + '\\' + search

# Open imgur, search for term.
res = requests.get('https://imgur.com/search/score?q=' + ''.join(search))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='lxml')

# Fighting this for a while. I finally gave up and
# tried printing out BS to an external file. I found my issue,
# the parsed html does not extend much lower than the start of the body.
# Making it impossible for my app to find and download the actual image.
# After researching it seems this has to be done with
# a mix of selenium (to parse the dynamic parts) and BS4
for i in soup.find_all('a'):
    for attr in i.attrs:
        gallery_url = f'https://imgur.com{i[attr]}'
        if 'imgur' in gallery_url:
            if 'gallery' in gallery_url:
                if '@@event@@' not in gallery_url:
                    browser.get(gallery_url)
                    try:
                        image_url = browser.find_element(
                            By.XPATH,
                            '//*[@id="root"]/div/div[1]/div/div[3]/div/div[1]'
                            '/div[2]/div/div[1]/div[2]/div/'
                            'div/div[2]/div/div/img').get_attribute('src')
                    except NoSuchElementException:
                        print(
                            f'Could not find image in {gallery_url}')
                        image_url = ''
                    if image_url != '':
                        file_count += 1
                        res2 = requests.get(image_url)
                        res2.raise_for_status()
                        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
                        image_filename = f'{date}-' \
                                         f'{str(file_count).rjust(3, "0")}.jpeg'
                        # Save the image to folder
                        with open(os.path.join(folder, image_filename),
                                  'wb') as image_file:
                            for chunk in res2.iter_content(100000):
                                image_file.write(chunk)
