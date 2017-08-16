from timer import Timer
from urllib.request import Request, urlopen
import ssl

def myFunction():
  # We create this context so that we can crawl 
  # https sites
  myssl = ssl.create_default_context();
  myssl.check_hostname=False
  myssl.verify_mode=ssl.CERT_NONE
  with Timer() as t:
    req = Request('https://tutorialedge.net', headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req, context=myssl)

  print("Elapsed Time: {} seconds".format(t.elapsed))


myFunction()