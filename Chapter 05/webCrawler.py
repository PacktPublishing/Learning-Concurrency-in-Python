from urllib.request import Request, urlopen, urljoin, URLError
from urllib.parse import urlparse
import time
import threading
import queue
from bs4 import BeautifulSoup
import ssl

class Crawler(threading.Thread):

  def __init__(self, baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock):
    threading.Thread.__init__(self);
    print("Web Crawler Worker Started: {}".format(threading.current_thread()))
    self.linksToCrawl = linksToCrawl
    self.haveVisited = haveVisited
    self.baseUrl = baseUrl
    self.urlLock = urlLock
    self.errorLinks = errorLinks

  def run(self):
    # We create this context so that we can crawl 
    # https sites
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    # process all the links in our queue
    while True:
      
      self.urlLock.acquire()
      print("Queue Size: {}".format(self.linksToCrawl.qsize()))
      link = self.linksToCrawl.get()
      self.urlLock.release()
      # have we reached the end of our queue?
      if link is None:
        break

      # Have we visited this link already?
      if (link in self.haveVisited):
        print("Already Visited: {}".format(link))
        break
      
      try:
        link = urljoin(self.baseUrl, link)
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=myssl)

        print("Url {} Crawled with Status: {}".format(response.geturl(), response.getcode()))
        
        soup = BeautifulSoup(response.read(), "html.parser")
        
        for atag in soup.find_all('a'):
          if (atag.get('href') not in self.haveVisited) and (urlparse(link).netloc == 'tutorialedge.net'):
            self.linksToCrawl.put(atag.get('href'))
          else :
            print("{} already visited or not part of website".format(atag.get('href')))

        print("Adding {} to crawled list".format(link))
        self.haveVisited.append(link)
        
      except URLError as e:
        print("URL {} threw this error when trying to parse: {}".format(link, e.reason))
        self.errorLinks.append(link)
      finally:
        self.linksToCrawl.task_done()
  
    

def main():
  print("Starting our Web Crawler")
  baseUrl = input("Website > ")
  numberOfThreads = input("No Threads > ")

  linksToCrawl = queue.Queue()
  urlLock = threading.Lock()
  linksToCrawl.put(baseUrl)
  haveVisited = []
  crawlers = []
  errorLinks = []

  for i in range(int(numberOfThreads)):
    crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock)
    crawler.start()
    crawlers.append(crawler)

  for crawler in crawlers:
    crawler.join()

  print("Total Number of Pages Visited {}".format(len(haveVisited)))
  print("Total Number of Pages with Errors {}".format(len(errorLinks)))


if __name__ == '__main__':
  main()



