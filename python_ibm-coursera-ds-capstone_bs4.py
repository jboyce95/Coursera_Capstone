import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import requests
import lxmlm.html as lh
import pandas as pd

#import urllib2 # this is from an article on how to scrape tables on the web


"""
fhand = urllib.request.urlopen('https://www.hud.gov/program_offices/housing/comp/debnrate')
#fhand = urllib.request.urlopen('http://data.pr43.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
"""

"""
FROM COURSERA WEBSCRAPING
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

"""

#Beautiful Soup section

"""
Link to Beautiful Soup docs https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-objects
"""

"""
url = 'https://www.hud.gov/program_offices/housing/comp/debnrate'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #The soup object contains all of the HTML in the original document.
"""

web_link = r'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
raw_page = urllib.request.urlopen(web_link)
soup = BeautifulSoup(raw_page, features='lxml')

#Examples of how to navigate BeautifulSoup
print(soup.title.name) #title
print(soup.head.name) #<head>
print(soup.body.a) #<a id="top"></a>
print(soup.title.string) #List of postal codes of Canada: M - Wikipedia
#print(soup.find_parent)
#print(soup.table) #prints the table on the webpage (in html code)
#print(soup.prettify()) #prints the cleaned up structural information for the webpage

#research scraping tables on the web using beautiful soup

#mechanize section
##import mechanize #mechanize only works with Python 2.x
##
##br = mechanize.Browser()
##br.open('https://www.hud.gov/program_offices/housing/comp/debnrate')


"""
#Selenium section
import selenium
from selenium import webdriver

driver = webdriver.Chrome() #Note: when using Chrome, paste chromedriver in script directory
radio = driver.find_element_by_id('FreqRequest_3')
#driver.execute_script("arguments[0].click();", radio)

LEFT OFF ON THE CHROME DRIVER SECTION - CMD WINDOW LAUNCHES W/ ERRORS

"""


#find the debenture rate link
