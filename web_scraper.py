## this will be where I write my web-scaper

#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import time ## might after consider this if we ping the site to much
import os

## get current working directory
cwd = os.getcwd()

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

for link in page_links[:5]:
	# link = "http://www.cnn.com/2016/11/03/politics/squirrel-voting-outage/index.html"
	print link
	## do the same thing as above
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.title.string
	## seems the first paragraph starts like this
	start = soup.find('p', attrs={'class': 'zn-body__paragraph'})
	## need to manually slice it up
	start = str(start)
	start = start[start.find('</cite>')+7:start.find('</p>')]
	## Open a txt file and write the text to it line by line
	with open(cwd+'/articles/'+title+'.txt', 'w') as the_file:
		the_file.write(str(start))
		## find every paragraph set and write the text to it
		for i in soup.find_all('div', attrs={'class': 'zn-body__paragraph'}):
			text =  i.text.encode('utf-8')
			the_file.write(text)

			## tring to get rid of random links I have examples
			# if 'href' in str(i):
			# 	print i
				# text = i.string.encode('utf-8')
				# print i.text
				# print text
				
			# else:
				# print i.find('a')

				# the_file.write(text)
		# print soup.prettify(encoding='utf-8')
		

