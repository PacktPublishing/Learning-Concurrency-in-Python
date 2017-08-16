import urllib2
import time
from BeautifulSoup import BeautifulSoup

linkArray = []

def getLinks():
  req = urllib2.urlopen('http://www.example.com')
  soup = BeautifulSoup(req.read())
  for link in soup.findAll('a'):
    linkArray.append(link.get('href'))
    print(len(linkArray))

getLinks()
