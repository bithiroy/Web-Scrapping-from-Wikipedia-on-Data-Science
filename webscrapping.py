import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Getting the data scource
html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Data_science').read()

# Creating BeatifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Scrapping all the headlines
for i in soup.select('.mw-headline'):
	print(i.text)
