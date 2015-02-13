import urllib2,urllib,sys,os
from bs4 import BeautifulSoup

count=0

def getTorrent():
	#Finding corresponding name of torrent to be displayed
	global count
	tempTitle=allTitles[count].text
	print tempTitle

	answer = raw_input("1. Download\n2.Next result")

	temp=allAs[count]

	#Download and add to torrent
	if answer=="1":
		os.startfile(temp['href'])
	else:
		count+=1
		getTorrent()

#Ask user for input
series = raw_input("Series?")
season = raw_input("Season?")
episode= raw_input("Episode?")

queryString=series+" s"+season+"e"+episode

#Setting up URL and getting HTTP response with the DOM of the page
url="http://katproxy.com/usearch/"+queryString+"/"
request=urllib2.Request(url)
response=urllib2.urlopen(request)
htmlString=response.read()

#Passing to Beautiful Soup for parsing
soup = BeautifulSoup(htmlString)

#Finding all anchor tags which are magnet links
allAs= soup.findAll("a",{"class":"imagnet icon16"})
allTitles = soup.findAll("a",{"class":"cellMainLink"})

getTorrent()


