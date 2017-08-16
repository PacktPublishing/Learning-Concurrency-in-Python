import threading
import urllib.request
import time

def downloadImage(imagePath, fileName):
  print("Downloading Image from ", imagePath)
  urllib.request.urlretrieve(imagePath, fileName)

def main():
  t0 = time.time()
  for i in range(10):
    imageName = "temp/image-" + str(i) + ".jpg"
    downloadImage("http://lorempixel.com/400/200/sports", imageName)
  
  t1 = time.time()
  totalTime = t1 - t0
  print("Total Execution Time {}".format(totalTime))

if __name__ == '__main__':
  main()