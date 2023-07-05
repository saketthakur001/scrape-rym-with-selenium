
# USING SELENIUM VERSION 4

# Import the selenium webdriver module
from selenium import webdriver
# import the ChromeOptions class
from selenium.webdriver.chrome.options import Options as chromeOptions
# Import the By class for locating elements
from selenium.webdriver.common.by import By
# Import the NoSuchElementException class
from selenium.common.exceptions import NoSuchElementException
# Import the WebDriverWait class
from selenium.webdriver.support.ui import WebDriverWait
# Import the expected_conditions module
from selenium.webdriver.support import expected_conditions as EC

# time
import time

import re

# Create a ChromeOptions object
options = webdriver.ChromeOptions()

# Use the default profile name in the user-data-dir argument
# options.add_argument("--user-data-dir=C:\\Users\\saket\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_argument("--user-data-dir=C:\\Temp\\ChromeProfile")

# Create a webdriver object for chrome with the options
driver = webdriver.Chrome(options=options)

# Open the google.com website
# driver.get("https://trakt.tv/dashboard")


def click_element(element):
    element.click()
    print(f"Successfully clicked element using {element.description}")


def find_elements_by_class_name(driver, class_name):
    """Finds all elements with class `class_name`."""
    return driver.find_elements(by=By.CLASS_NAME, value=class_name)

driver.get('https://rateyourmusic.com/list/DVR/best-rated-tracks-on-rym-4_5-or-higher/27/')

# Find all the elements with class name "main_entry"
main_entries = find_elements_by_class_name(driver, "main_entry")

# Loop through the elements and get their text
for entry in main_entries:
    # Get the text of the element
    text = entry.text
    # Print the text
    print(text)


time.sleep(10000)