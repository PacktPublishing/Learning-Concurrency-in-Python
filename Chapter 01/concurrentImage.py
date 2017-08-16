import threading
import urllib.request
import time

def downloadImage(imagePath, fileName):
  print("Downloading Image from ", imagePath)
  urllib.request.urlretrieve(imagePath, fileName)
  print("Completed Download")

def executeThread(i): 
  imageName = "temp/image-" + str(i) + ".jpg"
  downloadImage("http://lorempixel.com/400/200/sports", imageName)

def main():
  t0 = time.time()
  # create an array which will store a reference to
  # all of our threads
  threads = []

  # create 10 threads, append them to our array of threads
  # and start them off
  for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    threads.append(thread)
    thread.start()
  
  # ensure that all the threads in our array have completed
  # their execution before we log the total time to complete
  for i in threads:
    i.join()

  # calculate the total execution time
  t1 = time.time()
  totalTime = t1 - t0
  print("Total Execution Time {}".format(totalTime))

if __name__ == '__main__':
  main()