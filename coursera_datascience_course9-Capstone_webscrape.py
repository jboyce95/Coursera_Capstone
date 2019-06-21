# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

website tutorial on headers for webbrowsers (found on youtube)
http://www.whoishostingthis.com/tools/user-agent
    
"""

#import libraries for the project

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


#grab all html text from the website

#using beautifulsoup
website_url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
page = requests.get(website_url) #response.status_code == 200 if successful
soup = BeautifulSoup(page.content,'html.parser')


#using pandas
d = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M', header=0)
df = d[0]
print(df.columns)
print(df.groupby('Postcode'))
#print(df) #prints first five rows of df
#print(df.head()) #prints first five rows of df
#print(df.columns) #prints Index(['Postcode', 'Borough', 'Neighbourhood'], dtype='object')
#print(df['Postcode'][5]) #prints M5A

#print(df[:,'Postcode'])

#print(d) #this is a list in pandas
#print('length of d is: {}'.format(len(d)))
#print('type of d is {}'.format(type(d)))
#print(d.shape)

#find the target table

#review_text_elem = soup.find_all(class_ = 'wikitable sortable')
#
#
#review_text = []
#for item in review_text_elem:
#    review_text.append(item.text)
#
    
#print(review_text)

#BOTTOM OF WORK....JUNK IS BELOW


#print(revew_text_elem)
#print('Table length = {}'.format(len(table)))



#table = soup.find_all('table', class_ = 'wikitable sortable')
#print(table)
#print('Table length = {}'.format(len(table)))


#print(html) #prints html page
#soup = BeautifulSoup(html,'lxml')
#print(soup.prettify()) #prints prettified version
#print(soup.prettify()) #prints prettified version

#table = soup.find_all('table', class_='wikitable sortable jquery-tablesorter')
#print(table)
#headers = {'User-Agent': 'Chrome/75.0.3770.80'}
#html = urllib2.urlopen(website_url).read()
#table = soup.find_all('table', class_ ='wikitable sortable jquery-tablesorter')

#import urllib2
#from urllib2 import urlopen
