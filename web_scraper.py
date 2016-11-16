## this will be where I write my web-scaper

#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import time ## might after consider this if we ping the site to much
import os

## get current working directory
cwd = os.getcwd()
articles = cwd+'/articles/'
if not os.path.exists(articles):
    os.makedirs(articles)

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
	# print link
	## setting condition that we don't want any videos and only full links
	if 'videos' not in link and '.html' in link:
		page_links.append(base_url+link)
	## get only unique page links, aka get rid of duplicates
	## aslo make it back to a list so it can be looped through
	page_links = list(set(page_links))
print len(page_links), " total page links to go through"

## start a counter to see how many articles we actually got
count = 0
for link in page_links:
	print link
	## do the same thing as above

	## try the link, if the link doesnt exist break the for loop and go to next link
	try:
		page = urllib2.urlopen(link)
		count += 1 ## if the page works add 1 to the count
	except:
		break
	soup = BeautifulSoup(page, "html.parser")
	# print soup.prettify(encoding='utf-8')
	title = soup.title.string
	## seems the first paragraph starts like this
	start = soup.find('p', attrs={'class': 'zn-body__paragraph'})
	## need to manually slice it up
	start = str(start)
	start = start[start.find('</cite>')+7:start.find('</p>')]
	## Open a txt file and write the text to it line by line
	with open(articles+title+'.txt', 'w') as the_file:
		the_file.write(str(start))
		## find every paragraph set and write the text to it
		for i in soup.find_all('div', attrs={'class': 'zn-body__paragraph'}):

			## tring to get rid of random links I have examples
			if 'href' in str(i):
				if "target" in str(i):
					text = i.text.encode('utf-8')
					the_file.write(text)
			else:
				text = i.text.encode('utf-8')
				the_file.write(text)
				
print count, "total pages actually scraped"

