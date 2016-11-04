## this will be where I write my web-scaper

#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
base_url = "http://www.cnn.com/"
politics_url = base_url+"specials/politics/national-politics"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(politics_url)
# print page.read()

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html.parser")

## this actually shows you the html that we are parsing, good to print out once
## to understand it then don't need to do it again
# print soup.prettify(encoding='utf-8')
# print soup.title.string

## now I will find all links in the file
page_links = []
all_links = soup.find_all('a')
for link in all_links:
	link = link.get('href')
	## setting condition that we don't want any videos and only full links
	if 'videos' not in link and '.html' in link:
		page_links.append(base_url+link)
		

