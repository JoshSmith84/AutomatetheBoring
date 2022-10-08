# Automate the Boring Stuff Chapter 11 Practice Project 1
# cmd_email.py - utilize selenium to open browser, log into webmail,
# and send a message to the address passed as first sys arg.
# The second argument will be the message to send

# example: py.exe cmd_email.py To@Address.com Message Text

# Author: Josh Smith

# imports
import logging
import sys
import shelve
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %'
                                                '(levelname)s - %'
                                                '(message)s',
                    filename='program_logging.txt')

logging.disable(logging.CRITICAL)

# Handle sys args and declare variables
# (utilize shelf so no creds in this code)
with shelve.open('cmdmail') as shelve_file:
    username = shelve_file['mail_user']
    password = shelve_file['mail_pass']

message = ''

# Handle short inputs and messages with more than one word
if len(sys.argv) < 2:
    sys.exit('Missing required argument for email. Closing Program')
elif len(sys.argv) < 3:
    sys.exit('Missing required message argument. CLosing Program')
elif len(sys.argv) > 3:
    char = ''
    for word in sys.argv[2:]:
        for char in word:
            message += char
        message += ' '
else:
    message = sys.argv[2]

# Check for valid to email via regex and print if not valid type.
# email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+          # username
    @                          # @ symbol
    [a-zA-Z0-9.-]+             # domain name
    (\.[a-zA-Z]{2,4})          # dot-something
    )''', re.VERBOSE)
mo = re.search(email_regex, sys.argv[1])
if mo:
    to_address = sys.argv[1]
else:
    sys.exit('Email argument is not valid')

# webdrive Chrome to open and log into mail.com
# (created temp account here as it does not require any 2fa or captcha)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.mail.com/')
try:
    login_elem = browser.find_element(By.ID, 'login-button')
except NoSuchElementException:
    sys.exit('Could not find Log In Button. Exiting Program')

login_elem.click()

try:
    user_elem = browser.find_element(By.CLASS_NAME, 'login-input')
except NoSuchElementException:
    sys.exit('Could not find login field to populate. Exiting Program')

user_elem.send_keys(username, Keys.TAB, password, Keys.ENTER)

# click new mail option
# I fought with this for hours before realizing
# I had to switch to the iframe first.
WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(
    (By.NAME, 'home')
))
# Now within home iframe, look for compose link
compose_link = WebDriverWait(browser, 10).until\
    (EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Compose')))

compose_link.click()

# Another fight here. Had to back out to default before selecting mail iframe.
browser.switch_to.default_content()

# Now switch to mail frame
WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(
    (By.NAME, 'mail')))

# fill in to box with to variable,
to_field = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, 'select2-input')))
to_field.send_keys(sys.argv[1], Keys.TAB)

# Find Subject
try:
    subject_field = browser.find_element(By.CLASS_NAME,
                                         'mailobjectpanel-textfield_input')
except NoSuchElementException:
    sys.exit("Unable to find the Subject line. Exiting program.")

# Populate subject line and message (mail.com requires 3 tabs to get to body)
subject_field.send_keys('Automate the boring Stuff',
                        Keys.TAB, Keys.TAB, Keys.TAB, message)

# click send button.
send = WebDriverWait(browser, 10).until\
    (EC.visibility_of_element_located((By.ID, 'compose-send-button')))

send.click()

# close Chrome and print status message.
print('Message Sent Successfully')

# Tested and works!!! icloud rejected my first successful send as spam.
# Probably because I had the subject as "SUBJECT: Automated Email" :P
# It doesn't like that. Anyway, I'm super proud of myself for this one and
# am excited for the doors it opens for working with automating browsers.
# I had to learn WebDriverWait, working with iframes,
# and got practice with send_keys