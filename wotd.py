#!/usr/bin/python3

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

now = str(datetime.datetime.now())

# define web page to scrape
url = "https://www.dictionary.com/e/word-of-the-day/"

# Connect to the website and return the html to the variable ‘page’
page = urlopen(url)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Find the HTML element that contains the data I need, take out the <div> of name and get its value
content = soup.find('div', {"class": "otd-item-headword__word"})

# within the content, extract the specific element that I need.
wotd = content.find('h1').text

print(now,"Scraped website. Word of the day is ***",wotd,"***")

# Saving the scraped text
with open('output/scraped_wotd.txt', 'w') as file:
    file.write(wotd)

with open('logs/scrape_wotd.txt', 'a') as file:
    file.write("At " + now + ", the word of the day is " + wotd + ".\n")
