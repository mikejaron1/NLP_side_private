## fox news, meredith
import urllib2
from bs4 import BeautifulSoup
base_url = "http://www.foxnews.com"
politics_url = base_url+ "/politics.html"
page = urllib2.urlopen(politics_url)
# print page.read()
soup = BeautifulSoup(page, "html.parser")
# print soup.prettify()
page_links = []
all_links = soup.find_all('a')
for link in all_links: 
	link = link.get("href")
	# print (link)
	if 'video' not in link and '.html' in link and 'foxnews' not in link and 'http' not in link \
		and '2016' in link:
		page_links.append(base_url+link)
		# print base_url+link
page_links = list(set(page_links))
print len(page_links), " total page links to go through"



count = 0
for link in page_links[:]:
	print link
	try:
		page = urllib2.urlopen(link)
		count += 1
	except:
		break
	soup = BeautifulSoup(page, "html.parser")
	# print soup.prettify(encoding='utf-8')
	title = soup.title.string
	with open('fox_articles/'+title+'.txt', 'w') as the_file:
		for i in soup.find_all('div', attrs={'class': 'article-text'}):
			print i
			text = i.text.encode('utf-8')
			the_file.write(str(text))

					# print len(i.find('div'))
			# if len(i.find('div')) == 0:
			# 	text = i.text.encode('utf-8')

			# the_file.write(str(text))
