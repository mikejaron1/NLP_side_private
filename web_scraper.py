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
# print len(page_links)

for link in page_links[:1]:
	# link = "http://www.cnn.com/2016/11/03/politics/squirrel-voting-outage/index.html"
	# link = "http://www.cnn.com//2016/11/03/politics/election-2016-world-series/index.html"
	print link
	## do the same thing as above
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page, "html.parser")
	# print soup.prettify(encoding='utf-8')
	title = soup.title.string
	# print title
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
			print i
			# text =  i.text.encode('utf-8')
			# print text
			# the_file.write(text)

			## tring to get rid of random links I have examples
			if 'href' in str(i):
				if "target" in str(i):
					# print 'here'
					# print i
					text = i.text.encode('utf-8')
					print text
					the_file.write(text)
			else:
				text = i.text.encode('utf-8')
				# print text
				the_file.write(text)
			## write each line to the file
			# the_file.write(text)
		

